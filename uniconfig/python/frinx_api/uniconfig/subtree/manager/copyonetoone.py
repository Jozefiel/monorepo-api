# generated by datamodel-codegen:
#   filename:  uniconfigV3.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from ...frinx import types
from . import Datastore
from . import Operation


class Input(BaseModel):
    class Config:
        allow_population_by_field_name = True

    source_datastore: Optional[Datastore] = Field(None, alias='source-datastore')
    target_datastore: Optional[Datastore] = Field(None, alias='target-datastore')
    target_path: Optional[str] = Field(None, alias='target-path')
    """
    Target path under which data from source paths is put/merged.
    """
    operation: Optional[Operation] = None
    source_path: Optional[str] = Field(None, alias='source-path')
    """
    Source path to data which is put/merged under target nodes.
    """


class Output(BaseModel):
    class Config:
        allow_population_by_field_name = True

    result: Optional[types.OperationResultType] = None
    error_message: Optional[str] = Field(None, alias='error-message')
    """
    Error message describing operation failure.
    """
