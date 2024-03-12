# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .fine_tuning_response import FineTuningResponse
from .voice_response_model_safety_control import VoiceResponseModelSafetyControl
from .voice_sample import VoiceSample
from .voice_settings import VoiceSettings
from .voice_sharing_response import VoiceSharingResponse
from .voice_verification_response import VoiceVerificationResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class VoiceResponse(pydantic.BaseModel):
    voice_id: str
    name: str
    samples: typing.List[VoiceSample]
    category: str
    fine_tuning: FineTuningResponse
    labels: typing.Dict[str, str]
    description: str
    preview_url: str
    available_for_tiers: typing.List[str]
    settings: VoiceSettings
    sharing: VoiceSharingResponse
    high_quality_base_model_ids: typing.List[str]
    safety_control: typing.Optional[VoiceResponseModelSafetyControl] = None
    voice_verification: typing.Optional[VoiceVerificationResponse] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
