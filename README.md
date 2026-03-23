<div align="center">
<h1 align="center">MoneyPrinterTurbo-ES 💸</h1>

<p align="center">
  Fork en español de MoneyPrinterTurbo, pensado para creadores de contenido y negocios hispanohablantes.<br/>
  Mantenido por <a href="https://enjinia.es">Enjinia Tech</a>.
</p>

<p align="center">
  <a href="https://github.com/EnjiniaTech/MoneyPrinterTurbo-ES/stargazers"><img src="https://img.shields.io/github/stars/EnjiniaTech/MoneyPrinterTurbo-ES.svg?style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/EnjiniaTech/MoneyPrinterTurbo-ES/issues"><img src="https://img.shields.io/github/issues/EnjiniaTech/MoneyPrinterTurbo-ES.svg?style=for-the-badge" alt="Issues"></a>
  <a href="https://github.com/EnjiniaTech/MoneyPrinterTurbo-ES/blob/main/LICENSE"><img src="https://img.shields.io/github/license/EnjiniaTech/MoneyPrinterTurbo-ES.svg?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <a href="README-en.md">English README</a> ·
  <a href="https://github.com/EnjiniaTech/MoneyPrinterTurbo-ES/issues">Reportar un problema</a> ·
  <a href="https://enjinia.es">enjinia.es</a>
</p>

![WebUI](docs/webui-en.jpg)
</div>

---

## ¿Qué es?

Proporciona un tema o palabra clave y el proyecto genera automáticamente un vídeo corto completo: guion, material visual, voz sintetizada, subtítulos y música de fondo.

Este fork adapta el proyecto original al ecosistema hispanohablante. La interfaz está en español, las variantes de idioma cubren España y LATAM, y la integración con Gemini TTS y ElevenLabs está actualizada y funcional con las versiones actuales de sus APIs.

## Diferencias respecto al proyecto original

- Interfaz completamente en español
- Generación de vídeo en `es-ES` y `es-MX`
- Soporte actualizado para Gemini TTS (compatible con la API de 2024+)
- ElevenLabs integrado y configurable desde la interfaz
- Configuración de ejemplo orientada a español desde el primer momento
- Diseñado para despliegues con variables de entorno (Docker, Railway, cualquier PaaS)

## Funciones principales

- API REST y WebUI independientes con arquitectura MVC
- Generación de guion con IA o introducción manual
- Exportación en vertical `9:16` y horizontal `16:9`
- Generación por lotes
- Material de Pexels, Pixabay o archivos locales
- Compatibilidad con múltiples proveedores LLM: OpenAI, Gemini, Azure, Ollama, DeepSeek y otros
- Síntesis de voz: Azure TTS, Gemini TTS, ElevenLabs, SiliconFlow
- Subtítulos automáticos con `edge` (rápido) o `whisper` (mayor precisión)
- Música de fondo aleatoria o personalizada

---

## Instalación

### Opción 1: Docker (recomendado)

```bash
cp .env.example .env
# Edita .env con tus claves de API
docker compose up
```

- WebUI disponible en `http://localhost:8501`
- API disponible en `http://localhost:8080/docs`

Para desarrollo con el código fuente montado como volumen:

```bash
docker compose -f docker-compose.dev.yml up --build
```

### Opción 2: Instalación manual

**Dependencias del sistema:** `ffmpeg` e `ImageMagick`.

```bash
# macOS
brew install ffmpeg imagemagick

# Ubuntu / Debian
sudo apt-get install ffmpeg imagemagick
```

**Entorno Python:**

```bash
git clone https://github.com/EnjiniaTech/MoneyPrinterTurbo-ES.git
cd MoneyPrinterTurbo-ES
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp config.example.toml config.toml
```

Edita `config.toml` y define como mínimo el proveedor LLM y las claves de Pexels o Pixabay.

**Iniciar la WebUI:**

```bash
sh webui.sh        # macOS / Linux
webui.bat          # Windows
```

**Iniciar la API:**

```bash
python main.py
```

---

## Imagen Docker

La imagen está publicada en Docker Hub y puede usarse directamente sin necesidad de clonar el repositorio.

```bash
docker pull enjiniatech/moneyprinterturbo-es:latest
```

**WebUI:**

```bash
docker run --name mpt-webui \
  -p 8501:8501 \
  -e LLM_PROVIDER=openai \
  -e OPENAI_API_KEY=tu_api_key \
  -e OPENAI_MODEL_NAME=gpt-4o \
  -e PEXELS_API_KEYS=tu_pexels_key \
  -e UI_LANGUAGE=es \
  -v $(pwd)/storage:/MoneyPrinterTurbo/storage \
  enjiniatech/moneyprinterturbo-es:latest
```

**API:**

```bash
docker run --name mpt-api \
  -p 8080:8080 \
  -e LLM_PROVIDER=openai \
  -e OPENAI_API_KEY=tu_api_key \
  -e OPENAI_MODEL_NAME=gpt-4o \
  -e PEXELS_API_KEYS=tu_pexels_key \
  -v $(pwd)/storage:/MoneyPrinterTurbo/storage \
  enjiniatech/moneyprinterturbo-es:latest \
  /bin/sh -lc ./api.sh
```

---

## Variables de entorno

Tanto si usas Docker, Railway u otro PaaS, la configuración se gestiona mediante variables de entorno. El archivo `.env.example` incluye todas las disponibles; las más habituales son:

| Variable | Descripción |
|---|---|
| `LLM_PROVIDER` | `openai`, `gemini`, `azure`... |
| `OPENAI_API_KEY` | Clave del proveedor LLM |
| `OPENAI_BASE_URL` | Endpoint alternativo o proxy |
| `OPENAI_MODEL_NAME` | Modelo a utilizar |
| `PEXELS_API_KEYS` | Clave de Pexels |
| `PIXABAY_API_KEYS` | Clave de Pixabay |
| `GEMINI_API_KEY` | Para Gemini LLM o Gemini TTS |
| `ELEVENLABS_API_KEY` | Clave de ElevenLabs |
| `ELEVENLABS_MODEL_ID` | Modelo de ElevenLabs |
| `ELEVENLABS_VOICE_ID` | Voz de ElevenLabs |
| `UI_LANGUAGE` | `es` para español |
| `UI_TTS_SERVER` | Proveedor de voz por defecto |
| `UI_VOICE_NAME` | Voz por defecto |

---

## Voz y subtítulos

### Proveedores de voz

- Azure TTS (V1 y V2)
- Google Gemini TTS
- ElevenLabs
- SiliconFlow TTS

Gemini TTS requiere únicamente `GEMINI_API_KEY`. ElevenLabs requiere `ELEVENLABS_API_KEY`, `ELEVENLABS_MODEL_ID` y `ELEVENLABS_VOICE_ID`, aunque también es posible seleccionar la voz desde la interfaz si tu plan devuelve el listado de voces disponibles.

### Subtítulos

El modo se configura mediante `subtitle_provider` en `config.toml`:

- `edge` — generación rápida, sin requisitos especiales de hardware
- `whisper` — mayor fiabilidad, requiere descargar un modelo de ~3 GB

Si la descarga automática de Whisper falla, coloca el modelo manualmente en:

```
MoneyPrinterTurbo-ES/
  models/
    whisper-large-v3/
```

---

## Problemas frecuentes

**`ffmpeg` no encontrado**
Instálalo en el sistema o define `ffmpeg_path` en `config.toml`.

**Error con ImageMagick**
En macOS: `brew install imagemagick`. En Linux: `sudo apt-get install imagemagick`. En Windows, evita rutas con caracteres especiales.

**ImageMagick bloquea operaciones en `/tmp`**
Edita `policy.xml` (habitualmente en `/etc/ImageMagick-X/`) y modifica el valor `rights` de la entrada con `pattern="@"` de `none` a `read|write`.

**Demasiados archivos abiertos (`Errno 24`)**
```bash
ulimit -n 10240
```

---

## Licencia

Este fork mantiene la licencia del proyecto original. Consulta [LICENSE](LICENSE).
