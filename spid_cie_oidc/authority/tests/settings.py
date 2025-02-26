from spid_cie_oidc.entity.jwks import serialize_rsa_key, new_rsa_key

INTERMEDIARY_RSA = new_rsa_key()
INTERMEDIARY_JWK1 = serialize_rsa_key(INTERMEDIARY_RSA.priv_key, kind='private')
INTERMEDIARY_JWK1_pub = serialize_rsa_key(INTERMEDIARY_RSA.pub_key)

RP_METADATA_JWK1 = {'kty': 'RSA', 'n': 'w8H80eT2zrs2XQ-SApZG9TkuXDuIxANfCVHt4fFqNnOEZaCNWqlTQIo0JiSBE-QmzZ09TYP1BJpESuQf_PUeLRVPfYHsBVk5OYvhT27_nYlV7_1LsFGLxxsIa-hswMMzvW-1_huKLy6Fp0WP0ouUJAHsF_eYVtO1ApRhvlIVd5azM4k7t8Lh8lkCSdF1SfGHfXnXJRb-XensZ0cFSfe2Koq9mD7jpGLXlPpXxj8Ow0g7KYT5kVtWE5ULmNmO7BIN1Hx4HpggbbEGgC9FyjKw4GfFb-csnB-icBPf_60HomjrkFFt6vTjrcqQaHOj-sEjP36N8rMSBiMmiMSPnsHhMQ', 'e': 'AQAB', 'd': 'jEDxjcTZXBbgBV8Bgt7-qfW1FJoHDEFKFxhfMpHQQoETa-jTPhCxOD2MzYM8A-9kKc8tu9r-crTAl1PI42kPnMd283phixd5G5Tv8gSaGdnq-45ka0iRuC7TItUdDiMNb_2YzB4ZLGLNmaIKQJSGqCHEcQuRVyxJtTZwrXaMMOhDqJaWUvUQWF5C7g5O5mOVTkNKw6ujzhqcWa4N3NE-HwcbVW_9st4s1c_ng-DlwLTptaeM5j-LOeZMX1zcVlwYMi5ZkYYY6FHHjYI4nBWDtqhvf-64QaTv8exIjk8PcxHOwhfLTWiHPLk14af7U_pCzkP87WQCBgNfvt3WILQ5DQ', 'p': '75eNHkWaYQMgzVfFwif5uftSxqOhFU6VkxNKdqoRuFxJuVTO-M-vbQc3BwPxms2xrpizU6zGcoPGPvccDi0G040wZh34pWDVABMgGMKXKmeTwj8FuM1DzOVq8DKHmdrhk1gaQbPAP8JVOVYK7uh_lG5wmz3X-En1McMk-E8g8Ic', 'q': '0Sny6DLNtDP1_B9qiyCaMtRqPSAUZ1ohCZRlBT6-IGRR31Kt5S2JcVNDnF5w4dunlDY4nhIBZ0v0VyzWKgDXj6qrFY1pm1iE29gW227YsVRWQU8xWGpBwEu8nxNMr0u0zfe0QEGWU4RvNAsZPRa31HU87Vm7I3NSZ34DZsCZJoc', 'kid': 'HIvo33-Km7n03ZqKDJfWVnlFudsW28YhQZx5eaXtAKA'}
RP_METADATA_JWK1_pub = {'kty': 'RSA', 'n': 'w8H80eT2zrs2XQ-SApZG9TkuXDuIxANfCVHt4fFqNnOEZaCNWqlTQIo0JiSBE-QmzZ09TYP1BJpESuQf_PUeLRVPfYHsBVk5OYvhT27_nYlV7_1LsFGLxxsIa-hswMMzvW-1_huKLy6Fp0WP0ouUJAHsF_eYVtO1ApRhvlIVd5azM4k7t8Lh8lkCSdF1SfGHfXnXJRb-XensZ0cFSfe2Koq9mD7jpGLXlPpXxj8Ow0g7KYT5kVtWE5ULmNmO7BIN1Hx4HpggbbEGgC9FyjKw4GfFb-csnB-icBPf_60HomjrkFFt6vTjrcqQaHOj-sEjP36N8rMSBiMmiMSPnsHhMQ', 'e': 'AQAB', 'kid': 'HIvo33-Km7n03ZqKDJfWVnlFudsW28YhQZx5eaXtAKA'}

rp_onboarding_data = dict(
    name="RP Test",
    sub="http://rp-test.it/oidc/rp/",
    type="openid_relying_party",
    metadata_policy={"openid_relying_party": {"scopes": {"value": ["openid"]}}},
    is_active=True,
    jwks = [RP_METADATA_JWK1_pub]
)

rp_conf = {
    "sub": rp_onboarding_data["sub"],
    "jwks" : [RP_METADATA_JWK1],
    "metadata": {
        "openid_relying_party": {
            "application_type": "web",
            "client_registration_types": ["automatic"],
            "client_name": "Name of this service called http://rp-test.it/oidc/rp/",
            "contacts": ["ops@rp.example.it"],
            "grant_types": ["refresh_token", "authorization_code"],
            "redirect_uris": ["http://rp-test.it/oidc/rp/callback/"],
            "response_types": ["code"],
            "subject_type": "pairwise",
            "client_id": "http://rp-test.it/oidc/rp/",
            "jwks": {"keys": [RP_METADATA_JWK1_pub]},
        }
    },
    "authority_hints": ["http://testserver/"],
    "is_active": True,
}

intermediary_conf = {
    "sub": "http://intermediary-test",
    "metadata": {
        "federation_entity": {
            "contacts": ["ops@localhost"],
            "federation_api_endpoint": "http://intermediary-test/fetch",
            "homepage_uri": "http://intermediary-test",
            "name": "example Intermediate",
        }
    },
    "trust_marks": [],
    "authority_hints": ["http://testserver/"],
    "is_active": True,
    "jwks": [INTERMEDIARY_JWK1]
}
intermediary_onboarding_data = dict(
    name="intermediary-test",
    sub="http://intermediary-test",
    type="federation_entity",
    # metadata_policy = {"openid_relying_party": {"scopes": {"value": ["openid"]}}},
    is_active=True,
    jwks = [INTERMEDIARY_JWK1_pub]
)


TRUST_MARK_PAYLOAD = {
    "iss": "$.issuer_sub",
    "sub": "$.sub",
    "iat": 1579621160,
    "id": "https://www.spid.gov.it/certification/rp",
    "mark": "https://www.agid.gov.it/themes/custom/agid/logo.svg",
    "ref": "https://docs.italia.it/italia/spid/spid-regole-tecniche-oidc/it/stabile/index.html",
}

RP_PROFILE = {
    "name": "SPID Public SP",
    "profile_category": "openid_relying_party",
    "profile_id": "https://www.spid.gov.it/certification/rp",
    "trust_mark_template": TRUST_MARK_PAYLOAD,
}

RP_METADATA = {
    "openid_relying_party": {
        "application_type": "web",
        "client_registration_types": ["automatic"],
        "client_name": f"Name of this service called {rp_onboarding_data['sub']}",
        "contacts": ["ops@rp.example.it"],
        "grant_types": ["refresh_token", "authorization_code"],
        "jwks": {"keys": [RP_METADATA_JWK1_pub]},
        "redirect_uris": [f"{rp_onboarding_data['sub']}/callback/"],
        "response_types": ["code"],
        "subject_type": "pairwise",
    }
}
