# generated by datamodel-codegen:
#   filename:  uniconfigV3.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class TrustedCertificateItem(BaseModel):
    class Config:
        allow_population_by_field_name = True

    certificate: Optional[str] = None
    """
    An X.509 v3 certificate structure as specified by RFC5280, encoded using
    the Base64 format.
    """
    name: Optional[str] = None


class Input(BaseModel):
    class Config:
        allow_population_by_field_name = True

    trusted_certificate: Optional[list[TrustedCertificateItem]] = Field(
        None, alias='trusted-certificate'
    )
    """
    A list of trusted certificate. These cerfitifcates can be used by a server to
    authenticate clients, or by clients to authenticate servers.
    """