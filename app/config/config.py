import os
import shutil
import socket

import toml
from loguru import logger

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
config_file = f"{root_dir}/config.toml"


def _parse_env_value(raw_value, current_value):
    if isinstance(current_value, bool):
        return raw_value.strip().lower() in ("1", "true", "yes", "on")
    if isinstance(current_value, int):
        return int(raw_value)
    if isinstance(current_value, float):
        return float(raw_value)
    if isinstance(current_value, list):
        return [item.strip() for item in raw_value.split(",") if item.strip()]
    return raw_value


def _apply_env_mapping(target: dict, mapping: dict[str, tuple[str, object]]):
    for key, (env_name, default_value) in mapping.items():
        raw_value = os.getenv(env_name)
        if raw_value is None or raw_value == "":
            continue
        target[key] = _parse_env_value(raw_value, target.get(key, default_value))


def load_config():
    # fix: IsADirectoryError: [Errno 21] Is a directory: '/MoneyPrinterTurbo/config.toml'
    if os.path.isdir(config_file):
        shutil.rmtree(config_file)

    if not os.path.isfile(config_file):
        example_file = f"{root_dir}/config.example.toml"
        if os.path.isfile(example_file):
            shutil.copyfile(example_file, config_file)
            logger.info("copy config.example.toml to config.toml")

    logger.info(f"load config from file: {config_file}")

    try:
        _config_ = toml.load(config_file)
    except Exception as e:
        logger.warning(f"load config failed: {str(e)}, try to load as utf-8-sig")
        with open(config_file, mode="r", encoding="utf-8-sig") as fp:
            _cfg_content = fp.read()
            _config_ = toml.loads(_cfg_content)
    return _config_


def save_config():
    with open(config_file, "w", encoding="utf-8") as f:
        _cfg["app"] = app
        _cfg["azure"] = azure
        _cfg["siliconflow"] = siliconflow
        _cfg["ui"] = ui
        f.write(toml.dumps(_cfg))


_cfg = load_config()

_cfg.setdefault("app", {})
_cfg.setdefault("azure", {})
_cfg.setdefault("siliconflow", {})
_cfg.setdefault("ui", {"hide_log": False})

_apply_env_mapping(
    _cfg["app"],
    {
        "video_source": ("VIDEO_SOURCE", "pexels"),
        "hide_config": ("HIDE_CONFIG", False),
        "pexels_api_keys": ("PEXELS_API_KEYS", []),
        "pixabay_api_keys": ("PIXABAY_API_KEYS", []),
        "llm_provider": ("LLM_PROVIDER", "openai"),
        "pollinations_api_key": ("POLLINATIONS_API_KEY", ""),
        "pollinations_base_url": ("POLLINATIONS_BASE_URL", ""),
        "pollinations_model_name": ("POLLINATIONS_MODEL_NAME", ""),
        "openai_api_key": ("OPENAI_API_KEY", ""),
        "openai_base_url": ("OPENAI_BASE_URL", ""),
        "openai_model_name": ("OPENAI_MODEL_NAME", ""),
        "moonshot_api_key": ("MOONSHOT_API_KEY", ""),
        "moonshot_base_url": ("MOONSHOT_BASE_URL", ""),
        "moonshot_model_name": ("MOONSHOT_MODEL_NAME", ""),
        "oneapi_api_key": ("ONEAPI_API_KEY", ""),
        "oneapi_base_url": ("ONEAPI_BASE_URL", ""),
        "oneapi_model_name": ("ONEAPI_MODEL_NAME", ""),
        "g4f_model_name": ("G4F_MODEL_NAME", ""),
        "azure_api_key": ("AZURE_API_KEY", ""),
        "azure_base_url": ("AZURE_BASE_URL", ""),
        "azure_model_name": ("AZURE_MODEL_NAME", ""),
        "azure_api_version": ("AZURE_API_VERSION", ""),
        "gemini_api_key": ("GEMINI_API_KEY", ""),
        "gemini_model_name": ("GEMINI_MODEL_NAME", ""),
        "gemini_base_url": ("GEMINI_BASE_URL", ""),
        "elevenlabs_api_key": ("ELEVENLABS_API_KEY", ""),
        "elevenlabs_model_id": ("ELEVENLABS_MODEL_ID", "eleven_multilingual_v2"),
        "elevenlabs_voice_id": ("ELEVENLABS_VOICE_ID", ""),
        "qwen_api_key": ("QWEN_API_KEY", ""),
        "qwen_model_name": ("QWEN_MODEL_NAME", ""),
        "deepseek_api_key": ("DEEPSEEK_API_KEY", ""),
        "deepseek_base_url": ("DEEPSEEK_BASE_URL", ""),
        "deepseek_model_name": ("DEEPSEEK_MODEL_NAME", ""),
        "modelscope_api_key": ("MODELSCOPE_API_KEY", ""),
        "modelscope_base_url": ("MODELSCOPE_BASE_URL", ""),
        "modelscope_model_name": ("MODELSCOPE_MODEL_NAME", ""),
        "subtitle_provider": ("SUBTITLE_PROVIDER", "edge"),
        "endpoint": ("ENDPOINT", ""),
        "material_directory": ("MATERIAL_DIRECTORY", ""),
        "enable_redis": ("ENABLE_REDIS", False),
        "redis_host": ("REDIS_HOST", "localhost"),
        "redis_port": ("REDIS_PORT", 6379),
        "redis_db": ("REDIS_DB", 0),
        "redis_password": ("REDIS_PASSWORD", ""),
        "max_concurrent_tasks": ("MAX_CONCURRENT_TASKS", 5),
        "api_key": ("API_KEY", ""),
    },
)

_apply_env_mapping(
    _cfg["azure"],
    {
        "speech_key": ("AZURE_SPEECH_KEY", ""),
        "speech_region": ("AZURE_SPEECH_REGION", ""),
    },
)

_apply_env_mapping(
    _cfg["siliconflow"],
    {
        "api_key": ("SILICONFLOW_API_KEY", ""),
    },
)

_apply_env_mapping(
    _cfg["ui"],
    {
        "hide_log": ("UI_HIDE_LOG", False),
        "language": ("UI_LANGUAGE", "es"),
        "tts_server": ("UI_TTS_SERVER", "azure-tts-v1"),
        "voice_name": ("UI_VOICE_NAME", "es-ES-ElviraNeural-Female"),
        "font_name": ("UI_FONT_NAME", "MicrosoftYaHeiBold.ttc"),
        "text_fore_color": ("UI_TEXT_FORE_COLOR", "#FFFFFF"),
        "font_size": ("UI_FONT_SIZE", 60),
    },
)

listen_host = _parse_env_value(os.getenv("LISTEN_HOST", ""), "0.0.0.0") if os.getenv("LISTEN_HOST") else _cfg.get("listen_host", "0.0.0.0")
listen_port = (
    int(os.getenv("PORT") or os.getenv("LISTEN_PORT"))
    if (os.getenv("PORT") or os.getenv("LISTEN_PORT"))
    else _cfg.get("listen_port", 8080)
)
project_name = os.getenv("PROJECT_NAME", _cfg.get("project_name", "MoneyPrinterTurbo"))
project_description = os.getenv(
    "PROJECT_DESCRIPTION",
    _cfg.get(
        "project_description",
        "<a href='https://github.com/harry0703/MoneyPrinterTurbo'>https://github.com/harry0703/MoneyPrinterTurbo</a>",
    ),
)
project_version = os.getenv("PROJECT_VERSION", _cfg.get("project_version", "1.2.6"))
reload_debug = _parse_env_value(os.getenv("RELOAD_DEBUG", ""), False) if os.getenv("RELOAD_DEBUG") else False
app = _cfg.get("app", {})
whisper = _cfg.get("whisper", {})
proxy = _cfg.get("proxy", {})
azure = _cfg.get("azure", {})
siliconflow = _cfg.get("siliconflow", {})
ui = _cfg.get("ui", {"hide_log": False})

hostname = socket.gethostname()
log_level = os.getenv("LOG_LEVEL", _cfg.get("log_level", "DEBUG"))

imagemagick_path = app.get("imagemagick_path", "")
if imagemagick_path and os.path.isfile(imagemagick_path):
    os.environ["IMAGEMAGICK_BINARY"] = imagemagick_path

ffmpeg_path = app.get("ffmpeg_path", "")
if ffmpeg_path and os.path.isfile(ffmpeg_path):
    os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path

logger.info(f"{project_name} v{project_version}")
