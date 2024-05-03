# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import typing_extensions

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from ...core.unchecked_base_model import UncheckedBaseModel, UnionMetadata


class PronunciationDictionaryRule_Alias(UncheckedBaseModel):
    string_to_replace: str
    alias: str
    type: typing.Literal["alias"] = "alias"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


class PronunciationDictionaryRule_Phoneme(UncheckedBaseModel):
    string_to_replace: str
    phoneme: str
    alphabet: str
    type: typing.Literal["phoneme"] = "phoneme"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


PronunciationDictionaryRule = typing_extensions.Annotated[
    typing.Union[PronunciationDictionaryRule_Alias, PronunciationDictionaryRule_Phoneme],
    UnionMetadata(discriminant="type"),
]
