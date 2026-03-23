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

## Qué hace

Le das un tema o una palabra clave y genera un vídeo corto completo: guion, material visual, voz, subtítulos y música de fondo. Todo automatizado.

Este fork adapta el proyecto al ecosistema hispanohablante: la interfaz está en español, las voces y variantes de idioma apuntan a España y LATAM, y el soporte para Gemini TTS y ElevenLabs está integrado y funcionando con la API actual.

## Qué añade respecto al original

- Interfaz completamente en español
- Generación de vídeo en `es-ES` y `es-MX`
- Soporte corregido para Gemini TTS (compatible con la API de 2024+)
- ElevenLabs visible y configurable desde la UI
- Configuración de ejemplo orientada a español desde el primer momento
- Preparado para despliegue con variables de entorno (Docker, Railway, cualquier PaaS)

## Funciones principales

- API REST + WebUI independientes, arquitectura MVC limpia
- Guion generado por IA o manual
- Exportación en vertical `9:16` y horizontal `16:9`
- Generación por lotes
- Material de Pexels, Pixabay o archivos locales propios
- Múltiples proveedores LLM: OpenAI, Gemini, Azure, Ollama, DeepSeek y más
- Síntesis de voz: Azure TTS, Gemini TTS, ElevenLabs, SiliconFlow
- Subtítulos automáticos con `edge` (rápido) o `whisper` (más preciso)
- Música de fondo aleatoria o personalizada

---

## Inicio rápido

### Opción 1: Docker (recomendado)

Es la forma más sencilla si no quieres tocar el entorno local.

```bash
cp .env.example .env
# Edita .env con tus claves
docker compose up
```

- WebUI: `http://localhost:8501`
- API: `http://localhost:8080/docs`

Para desarrollo con código fuente montado:

```bash
docker compose -f docker-compose.dev.yml up --build
```

### Opción 2: Instalación manual

**Requisitos del sistema:** `ffmpeg` e `ImageMagick`.

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

Edita `config.toml` y configura al menos tu proveedor LLM y las claves de Pexels o Pixabay.

**Arrancar la WebUI:**

```bash
sh webui.sh        # macOS / Linux
webui.bat          # Windows
```

**Arrancar la API:**

```bash
python main.py
```

---

## Despliegue con Docker Hub

La imagen está publicada en Docker Hub. Puedes tirar de ella directamente sin clonar el repositorio.

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

La imagen se publica automáticamente desde GitHub Actions cuando hay cambios en `main` o cuando se empuja un tag semántico (`v1.2.7`). Para activarlo en tu fork, añade los secrets `DOCKERHUB_USERNAME` y `DOCKERHUB_TOKEN` en la configuración del repositorio.

---

## Despliegue en Railway

Conecta el repositorio directamente en Railway. No necesitas Docker Compose, Railway gestiona cada servicio por separado.

Crea un servicio para la WebUI y, si quieres exponer la API también, un segundo servicio apuntando al mismo repositorio.

**Start commands:**

```bash
./webui.sh   # servicio WebUI
./api.sh     # servicio API
```

Configura las variables desde el panel de Railway. Puedes usar `.env.example` como referencia para saber qué necesitas. Las más habituales:

| Variable | Descripción |
|---|---|
| `LLM_PROVIDER` | `openai`, `gemini`, `azure`... |
| `OPENAI_API_KEY` | Clave del proveedor LLM |
| `OPENAI_BASE_URL` | Si usas un proxy o endpoint alternativo |
| `OPENAI_MODEL_NAME` | Modelo a usar |
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

### Proveedores de voz soportados

- Azure TTS (V1 y V2)
- Google Gemini TTS
- ElevenLabs
- SiliconFlow TTS

Para Gemini TTS basta con `GEMINI_API_KEY`. Para ElevenLabs necesitas `ELEVENLABS_API_KEY`, `ELEVENLABS_MODEL_ID` y `ELEVENLABS_VOICE_ID` (o seleccionar la voz desde la UI si tu plan devuelve el listado de voces).

### Subtítulos

Hay dos modos configurables en `subtitle_provider` dentro de `config.toml`:

- `edge`: más rápido, sin requisitos especiales de hardware
- `whisper`: más fiable en casos difíciles, requiere descargar un modelo de ~3 GB

Si usas `whisper` y la descarga automática falla, coloca el modelo manualmente en:

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
En macOS: `brew install imagemagick`. En Linux: `sudo apt-get install imagemagick`. Evita rutas con caracteres especiales en Windows.

**ImageMagick bloquea operaciones en `/tmp`**
Edita `policy.xml` (normalmente en `/etc/ImageMagick-X/`) y cambia `rights="none"` a `rights="read|write"` en la línea con `pattern="@"`.

**Demasiados archivos abiertos (`Errno 24`)**
```bash
ulimit -n 10240
```

---

## Hoja de ruta

- Más presets y voces para el mercado hispano
- Mejoras en el flujo de UGC y shorts en español
- Plantillas y defaults para distintos formatos de contenido

---

## Licencia

Este fork mantiene la licencia del proyecto original. Consulta [LICENSE](LICENSE).
