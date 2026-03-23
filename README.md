<div align="center">
<h1 align="center">MoneyPrinterTurbo-ES 💸</h1>

<p align="center">
  Fork hispano de MoneyPrinterTurbo con interfaz en español, mejor soporte de voces y enfoque para creadores y negocios hispanohablantes.
</p>

<p align="center">
  Mantenido por <a href="https://enjinia.es">Enjinia Tech</a><br/>
  <a href="https://github.com/EnjiniaTech/MoneyPrinterTurbo-ES">Repositorio</a> ·
  <a href="https://github.com/EnjiniaTech/MoneyPrinterTurbo-ES/issues">Issues</a> ·
  <a href="https://enjinia.es">enjinia.es</a> ·
  <a href="README-en.md">README en inglés</a>
</p>

![WebUI](docs/webui-en.jpg)
</div>

## Qué es

MoneyPrinterTurbo-ES genera vídeos cortos a partir de un tema o palabra clave. El flujo actual permite:

- generar guion y palabras clave con IA
- buscar material visual en Pexels, Pixabay o archivos locales
- sintetizar voz
- crear subtítulos
- añadir música de fondo
- renderizar el vídeo final en formato vertical u horizontal

Este fork adapta el proyecto al mercado hispanohablante y prioriza una experiencia más usable para España y LATAM.
Está mantenido por `Enjinia Tech` y pensado como una distribución pública más lista para usar, desplegar y adaptar a proyectos reales de contenido en español.

## Qué añade este fork

- interfaz traducida al español
- español disponible como idioma de generación
- soporte visible en la UI para Gemini TTS y ElevenLabs
- corrección del flujo de Gemini TTS con la API actual
- base preparada para voces y vídeos en español desde la configuración inicial

## Funciones principales

- arquitectura MVC con API y WebUI
- generación automática de guion o uso de guion manual
- exportación en `9:16` y `16:9`
- generación por lotes
- configuración de duración máxima de clips
- múltiples motores LLM
- múltiples proveedores de voz
- subtítulos con `edge` o `whisper`
- música aleatoria o personalizada
- uso de material local si no quieres depender de bancos de vídeo

## Requisitos

- macOS 11+, Windows 10+ o Linux moderno
- mínimo recomendado: `4 CPU` y `4 GB RAM`
- `ffmpeg`
- `ImageMagick` para algunas operaciones de render

## Inicio rápido

### 1. Clona el fork

```bash
git clone https://github.com/EnjiniaTech/MoneyPrinterTurbo-ES.git
cd MoneyPrinterTurbo-ES
```

### 2. Elige cómo vas a configurarlo

#### Opción A: desarrollo local clásico

```bash
cp config.example.toml config.toml
```

En `config.toml` configura al menos:

- `pexels_api_keys` o `pixabay_api_keys`
- un proveedor LLM
- si vas a usar Gemini TTS o ElevenLabs, sus claves correspondientes

#### Opción B: despliegue con Docker o Railway

Usa variables de entorno. Este fork está preparado para leer primero las variables del entorno y después `config.toml`.

Las más habituales son:

- `LLM_PROVIDER`
- `OPENAI_API_KEY`
- `OPENAI_BASE_URL`
- `OPENAI_MODEL_NAME`
- `PEXELS_API_KEYS`
- `PIXABAY_API_KEYS`
- `GEMINI_API_KEY`
- `ELEVENLABS_API_KEY`
- `ELEVENLABS_MODEL_ID`
- `ELEVENLABS_VOICE_ID`
- `UI_LANGUAGE`
- `UI_TTS_SERVER`
- `UI_VOICE_NAME`

## Despliegue manual

### 1. Crea un entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Instala dependencias del sistema

#### macOS

```bash
brew install ffmpeg imagemagick
```

#### Ubuntu / Debian

```bash
sudo apt-get update
sudo apt-get install ffmpeg imagemagick
```

### 3. Lanza la WebUI

```bash
sh webui.sh
```

La interfaz suele quedar en:

- `http://127.0.0.1:8501`

### 4. Lanza la API

```bash
python main.py
```

La documentación interactiva suele quedar en:

- `http://127.0.0.1:8080/docs`

## Docker Hub y contenedores

El camino principal para usuarios externos es:

- hacer `docker pull`
- usar la imagen publicada en Docker Hub
- pasar variables por `.env` o `-e`
- persistir `storage/` fuera del contenedor

### Descargar la imagen

```bash
docker pull enjiniatech/moneyprinterturbo-es:latest
```

### docker run para WebUI

```bash
docker run --name moneyprinterturbo-es-webui \
  -p 8501:8501 \
  -e PORT=8501 \
  -e LISTEN_HOST=0.0.0.0 \
  -e UI_LANGUAGE=es \
  -e LLM_PROVIDER=openai \
  -e OPENAI_API_KEY=tu_api_key \
  -e OPENAI_MODEL_NAME=gpt-5 \
  -e PEXELS_API_KEYS=tu_pexels_key \
  -v $(pwd)/storage:/MoneyPrinterTurbo/storage \
  enjiniatech/moneyprinterturbo-es:latest
```

### docker run para API

```bash
docker run --name moneyprinterturbo-es-api \
  -p 8080:8080 \
  -e PORT=8080 \
  -e LISTEN_HOST=0.0.0.0 \
  -e LLM_PROVIDER=openai \
  -e OPENAI_API_KEY=tu_api_key \
  -e OPENAI_MODEL_NAME=gpt-5 \
  -e PEXELS_API_KEYS=tu_pexels_key \
  -v $(pwd)/storage:/MoneyPrinterTurbo/storage \
  enjiniatech/moneyprinterturbo-es:latest \
  /bin/sh -lc ./api.sh
```

### Docker Compose

`docker-compose.yml` es ahora el camino principal para uso real con imagen publicada.

```bash
cp .env.example .env
docker compose up
```

Después:

- WebUI: `http://127.0.0.1:8501`
- API: `http://127.0.0.1:8080/docs`

Si quieres desarrollo local montando el código fuente:

```bash
docker compose -f docker-compose.dev.yml up --build
```

## Publicación automática en Docker Hub

El repositorio ya incluye workflow de GitHub Actions para publicar la imagen en Docker Hub cuando haya cambios en `main` o cuando publiques un tag.

### Secrets necesarios en GitHub

Configura estos secrets en el repositorio:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

### Qué hace el workflow

- construye la imagen con `Docker Buildx`
- publica en `docker.io/enjiniatech/moneyprinterturbo-es`
- genera `latest` desde `main`
- genera tags semánticos cuando empujes versiones tipo `v1.2.7`

### Ruta del workflow

```text
.github/workflows/docker-publish.yml
```

## Despliegue en Railway

La forma correcta de desplegar este fork en Railway es `env-first`.

### Qué hacer

1. Conecta el repositorio a Railway.
2. Crea un servicio para la `WebUI`.
3. Si quieres exponer la API también, crea un segundo servicio apuntando al mismo repo.
4. Usa las variables de [.env.example](/Users/fabiannitka/code/MoneyPrinterTurbo/.env.example) como referencia.

### Variables

Railway funciona mejor si configuras variables como:

- `OPENAI_API_KEY`
- `OPENAI_BASE_URL`
- `OPENAI_MODEL_NAME`
- `GEMINI_API_KEY`
- `PEXELS_API_KEYS`
- `PIXABAY_API_KEYS`
- `AZURE_SPEECH_KEY`
- `AZURE_SPEECH_REGION`
- `ELEVENLABS_API_KEY`
- `ELEVENLABS_MODEL_ID`
- `ELEVENLABS_VOICE_ID`
- `UI_LANGUAGE`
- `UI_TTS_SERVER`
- `UI_VOICE_NAME`

### Start command recomendado

Para la WebUI:

```bash
./webui.sh
```

Para la API:

```bash
./api.sh
```

### Nota importante

Railway no necesita `docker-compose` para desplegar este proyecto. El `compose` es útil para usuarios finales o despliegues propios, pero en Railway lo normal es desplegar servicios separados desde el mismo repo o la misma imagen.

## Voz y subtítulos

### Proveedores de voz

Actualmente el proyecto soporta:

- Azure TTS V1
- Azure TTS V2
- SiliconFlow TTS
- Google Gemini TTS
- ElevenLabs

### Gemini TTS

Para usar Gemini TTS necesitas configurar `GEMINI_API_KEY`.

Puedes hacerlo en:

- variables de entorno
- `config.toml`
- o desde la interfaz si estás trabajando en local

### ElevenLabs

Para usar ElevenLabs necesitas:

- `ELEVENLABS_API_KEY`
- `ELEVENLABS_MODEL_ID`
- `ELEVENLABS_VOICE_ID` o seleccionar una voz desde la UI si tu cuenta devuelve el listado

Puedes definirlos por variables de entorno o en `config.toml`.

### Subtítulos

Hay dos modos:

- `edge`: más rápido y ligero
- `whisper`: más pesado, pero más fiable

Se cambia desde `subtitle_provider` en `config.toml`.

## Vídeos en español

Este fork ya deja el proyecto orientado a español:

- UI por defecto en español
- idiomas de vídeo con variantes `es-ES` y `es-MX`
- voz española por defecto en la configuración de ejemplo
- soporte para cadenas y copy en español en el flujo principal

## Problemas frecuentes

### No se encuentra `ffmpeg`

Instálalo en el sistema o define `ffmpeg_path` en `config.toml`.

### Error con `ImageMagick`

Instala `ImageMagick` y evita rutas problemáticas. En macOS suele bastar con:

```bash
brew install imagemagick
```

### Whisper no descarga el modelo

Si no puede descargarlo automáticamente, puedes colocarlo manualmente en:

```text
MoneyPrinterTurbo-ES/
  models/
    whisper-large-v3/
```

## Hoja de ruta del fork

- pulir más textos de UI y mensajes auxiliares
- ampliar presets para voces hispanas
- mejorar el flujo de UGC y shorts en español
- añadir más plantillas y defaults para creadores y negocios hispanohablantes

## Licencia

Este fork mantiene la licencia del proyecto original. Consulta [LICENSE](LICENSE).
