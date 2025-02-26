from typing import List

from pydantic import BaseModel, HttpUrl, EmailStr


class FAMetadata(BaseModel):
    contacts: List[EmailStr]
    federation_api_endpoint: HttpUrl
    homepage_uri: HttpUrl
    name: str
