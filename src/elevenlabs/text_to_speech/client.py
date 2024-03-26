# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..types.optimize_streaming_latency import OptimizeStreamingLatency
from ..types.output_format import OutputFormat
from ..types.pronunciation_dictionary_version_locator import PronunciationDictionaryVersionLocator
from ..types.voice_settings import VoiceSettings

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TextToSpeechClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def convert(
        self,
        voice_id: str,
        *,
        optimize_streaming_latency: OptimizeStreamingLatency,
        output_format: OutputFormat,
        text: str,
        model_id: typing.Optional[str] = OMIT,
        voice_settings: typing.Optional[VoiceSettings] = OMIT,
        pronunciation_dictionary_locators: typing.Optional[
            typing.Sequence[PronunciationDictionaryVersionLocator]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Converts text into speech using a voice of your choice and returns audio.

        Parameters:
            - voice_id: str. Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

            - optimize_streaming_latency: OptimizeStreamingLatency. You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model.

            - output_format: OutputFormat. The output format of the generated audio.

            - text: str. The text that will get converted into speech.

            - model_id: typing.Optional[str]. Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

            - voice_settings: typing.Optional[VoiceSettings]. Voice settings overriding stored setttings for the given voice. They are applied only on the given request.

            - pronunciation_dictionary_locators: typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]. A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs import PronunciationDictionaryVersionLocator, VoiceSettings
        from elevenlabs.client import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.text_to_speech.convert(
            voice_id="string",
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text="string",
            model_id="string",
            voice_settings=VoiceSettings(
                stability=1.1,
                similarity_boost=1.1,
                style=1.1,
                use_speaker_boost=True,
            ),
            pronunciation_dictionary_locators=[
                PronunciationDictionaryVersionLocator(
                    pronunciation_dictionary_id="string",
                    version_id="string",
                )
            ],
        )
        """
        _request: typing.Dict[str, typing.Any] = {"text": text}
        if model_id is not OMIT:
            _request["model_id"] = model_id
        if voice_settings is not OMIT:
            _request["voice_settings"] = voice_settings
        if pronunciation_dictionary_locators is not OMIT:
            _request["pronunciation_dictionary_locators"] = pronunciation_dictionary_locators
        with self._client_wrapper.httpx_client.stream(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/text-to-speech/{jsonable_encoder(voice_id)}"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "optimize_streaming_latency": optimize_streaming_latency,
                        "output_format": output_format,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        ) as _response:
            if 200 <= _response.status_code < 300:
                for _chunk in _response.iter_bytes():
                    yield _chunk
                return
            _response.read()
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    def convert_as_stream(
        self,
        voice_id: str,
        *,
        optimize_streaming_latency: OptimizeStreamingLatency,
        output_format: OutputFormat,
        text: str,
        model_id: typing.Optional[str] = OMIT,
        voice_settings: typing.Optional[VoiceSettings] = OMIT,
        pronunciation_dictionary_locators: typing.Optional[
            typing.Sequence[PronunciationDictionaryVersionLocator]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Converts text into speech using a voice of your choice and returns audio as an audio stream.

        Parameters:
            - voice_id: str. Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

            - optimize_streaming_latency: OptimizeStreamingLatency. You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model.

            - output_format: OutputFormat. The output format of the generated audio.

            - text: str. The text that will get converted into speech.

            - model_id: typing.Optional[str]. Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

            - voice_settings: typing.Optional[VoiceSettings]. Voice settings overriding stored setttings for the given voice. They are applied only on the given request.

            - pronunciation_dictionary_locators: typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]. A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs import PronunciationDictionaryVersionLocator, VoiceSettings
        from elevenlabs.client import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.text_to_speech.convert_as_stream(
            voice_id="string",
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text="string",
            model_id="string",
            voice_settings=VoiceSettings(
                stability=1.1,
                similarity_boost=1.1,
                style=1.1,
                use_speaker_boost=True,
            ),
            pronunciation_dictionary_locators=[
                PronunciationDictionaryVersionLocator(
                    pronunciation_dictionary_id="string",
                    version_id="string",
                )
            ],
        )
        """
        _request: typing.Dict[str, typing.Any] = {"text": text}
        if model_id is not OMIT:
            _request["model_id"] = model_id
        if voice_settings is not OMIT:
            _request["voice_settings"] = voice_settings
        if pronunciation_dictionary_locators is not OMIT:
            _request["pronunciation_dictionary_locators"] = pronunciation_dictionary_locators
        with self._client_wrapper.httpx_client.stream(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/text-to-speech/{jsonable_encoder(voice_id)}/stream"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "optimize_streaming_latency": optimize_streaming_latency,
                        "output_format": output_format,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        ) as _response:
            if 200 <= _response.status_code < 300:
                for _chunk in _response.iter_bytes():
                    yield _chunk
                return
            _response.read()
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTextToSpeechClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def convert(
        self,
        voice_id: str,
        *,
        optimize_streaming_latency: OptimizeStreamingLatency,
        output_format: OutputFormat,
        text: str,
        model_id: typing.Optional[str] = OMIT,
        voice_settings: typing.Optional[VoiceSettings] = OMIT,
        pronunciation_dictionary_locators: typing.Optional[
            typing.Sequence[PronunciationDictionaryVersionLocator]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Converts text into speech using a voice of your choice and returns audio.

        Parameters:
            - voice_id: str. Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

            - optimize_streaming_latency: OptimizeStreamingLatency. You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model.

            - output_format: OutputFormat. The output format of the generated audio.

            - text: str. The text that will get converted into speech.

            - model_id: typing.Optional[str]. Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

            - voice_settings: typing.Optional[VoiceSettings]. Voice settings overriding stored setttings for the given voice. They are applied only on the given request.

            - pronunciation_dictionary_locators: typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]. A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs import PronunciationDictionaryVersionLocator, VoiceSettings
        from elevenlabs.client import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )
        await client.text_to_speech.convert(
            voice_id="string",
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text="string",
            model_id="string",
            voice_settings=VoiceSettings(
                stability=1.1,
                similarity_boost=1.1,
                style=1.1,
                use_speaker_boost=True,
            ),
            pronunciation_dictionary_locators=[
                PronunciationDictionaryVersionLocator(
                    pronunciation_dictionary_id="string",
                    version_id="string",
                )
            ],
        )
        """
        _request: typing.Dict[str, typing.Any] = {"text": text}
        if model_id is not OMIT:
            _request["model_id"] = model_id
        if voice_settings is not OMIT:
            _request["voice_settings"] = voice_settings
        if pronunciation_dictionary_locators is not OMIT:
            _request["pronunciation_dictionary_locators"] = pronunciation_dictionary_locators
        async with self._client_wrapper.httpx_client.stream(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/text-to-speech/{jsonable_encoder(voice_id)}"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "optimize_streaming_latency": optimize_streaming_latency,
                        "output_format": output_format,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        ) as _response:
            if 200 <= _response.status_code < 300:
                async for _chunk in _response.aiter_bytes():
                    yield _chunk
                return
            await _response.aread()
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    async def convert_as_stream(
        self,
        voice_id: str,
        *,
        optimize_streaming_latency: OptimizeStreamingLatency,
        output_format: OutputFormat,
        text: str,
        model_id: typing.Optional[str] = OMIT,
        voice_settings: typing.Optional[VoiceSettings] = OMIT,
        pronunciation_dictionary_locators: typing.Optional[
            typing.Sequence[PronunciationDictionaryVersionLocator]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Converts text into speech using a voice of your choice and returns audio as an audio stream.

        Parameters:
            - voice_id: str. Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

            - optimize_streaming_latency: OptimizeStreamingLatency. You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model.

            - output_format: OutputFormat. The output format of the generated audio.

            - text: str. The text that will get converted into speech.

            - model_id: typing.Optional[str]. Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

            - voice_settings: typing.Optional[VoiceSettings]. Voice settings overriding stored setttings for the given voice. They are applied only on the given request.

            - pronunciation_dictionary_locators: typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]. A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs import PronunciationDictionaryVersionLocator, VoiceSettings
        from elevenlabs.client import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )
        await client.text_to_speech.convert_as_stream(
            voice_id="string",
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text="string",
            model_id="string",
            voice_settings=VoiceSettings(
                stability=1.1,
                similarity_boost=1.1,
                style=1.1,
                use_speaker_boost=True,
            ),
            pronunciation_dictionary_locators=[
                PronunciationDictionaryVersionLocator(
                    pronunciation_dictionary_id="string",
                    version_id="string",
                )
            ],
        )
        """
        _request: typing.Dict[str, typing.Any] = {"text": text}
        if model_id is not OMIT:
            _request["model_id"] = model_id
        if voice_settings is not OMIT:
            _request["voice_settings"] = voice_settings
        if pronunciation_dictionary_locators is not OMIT:
            _request["pronunciation_dictionary_locators"] = pronunciation_dictionary_locators
        async with self._client_wrapper.httpx_client.stream(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/text-to-speech/{jsonable_encoder(voice_id)}/stream"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "optimize_streaming_latency": optimize_streaming_latency,
                        "output_format": output_format,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        ) as _response:
            if 200 <= _response.status_code < 300:
                async for _chunk in _response.aiter_bytes():
                    yield _chunk
                return
            await _response.aread()
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)
