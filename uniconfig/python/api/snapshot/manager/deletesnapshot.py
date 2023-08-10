# generated by datamodel-codegen:
#   filename:  uniconfigV3.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from ...frinx import types


class Input(BaseModel):
    class Config:
        allow_population_by_field_name = True

    name: Optional[str] = None
    """
    Name of snapshot.
    """


class Output(BaseModel):
    class Config:
        allow_population_by_field_name = True

    error_message: Optional[str] = Field(None, alias='error-message')
    """
    Error message that describe overall problem.
    """
    overall_status: types.OperationResultType = Field(..., alias='overall-status')
