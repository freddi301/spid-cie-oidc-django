import logging

from django.conf import settings
from django.core.exceptions import ValidationError
from spid_cie_oidc.entity.statements import (
    get_entity_configurations,
    EntityConfiguration,
)

from spid_cie_oidc.entity import settings as entity_settings
from spid_cie_oidc.entity.exceptions import MissingAuthorityHintsClaim, NotDescendant


logger = logging.getLogger(__name__)
HTTPC_PARAMS = getattr(settings, "HTTPC_PARAMS", entity_settings.HTTPC_PARAMS)
try:
    OIDCFED_TRUST_ANCHORS = getattr(settings, "OIDCFED_TRUST_ANCHORS")
except AttributeError:
    OIDCFED_TRUST_ANCHORS = []
    logger.warning("OIDCFED_TRUST_ANCHORS not configured in your settings file.")


def validate_entity_configuration(value):
    """
    value is the sub url
    """
    try:
        jwt = get_entity_configurations(value)[0]
    except Exception as e:
        raise ValidationError(f"Failed to fetch Entity Configuration for {value}: {e}")
    ec = EntityConfiguration(jwt, httpc_params=HTTPC_PARAMS)
    ec.validate_by_itself()

    authority_hints = ec.payload.get("authority_hints", [])
    if not authority_hints:
        raise MissingAuthorityHintsClaim(
            "authority_hints must be present in a descendant entity configuration"
        )
    proper_descendant = False
    for i in authority_hints:
        if i in OIDCFED_TRUST_ANCHORS:
            proper_descendant = True
            break
    if not proper_descendant:
        raise NotDescendant(
            "This participant MUST have one of "
            f"{', '.join(OIDCFED_TRUST_ANCHORS) or []} in "
            f"its authority_hints claim. It has: {authority_hints}"
        )
