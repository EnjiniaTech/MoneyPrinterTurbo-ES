<div align="center">
<h1 align="center">MoneyPrinterTurbo-ES 💸</h1>

<p align="center">
  Fork hispano de MoneyPrinterTurbo con interfaz en español, mejor soporte de voces y enfoque para creadores y negocios hispanohablantes.
</p>

<p align="center">
  <a href="https://github.com/EnjiniaTech/MoneyPrinterTurbo-ES">Repositorio</a> ·
  <a href="https://github.com/EnjiniaTech/MoneyPrinterTurbo-ES/issues">Issues</a> ·
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

### 2. Crea tu configuración local

```bash
cp config.example.toml config.toml
```

En `config.toml` configura al menos:

- `pexels_api_keys` o `pixabay_api_keys`
- un proveedor LLM
- si vas a usar Gemini TTS o ElevenLabs, sus claves correspondientes

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

## Despliegue con Docker

```bash
docker compose up
```

Después:

- WebUI: `http://127.0.0.1:8501`
- API: `http://127.0.0.1:8080/docs`

## Voz y subtítulos

### Proveedores de voz

Actualmente el proyecto soporta:

- Azure TTS V1
- Azure TTS V2
- SiliconFlow TTS
- Google Gemini TTS
- ElevenLabs

### Gemini TTS

Para usar Gemini TTS necesitas completar la `Gemini API Key` en los ajustes básicos de la interfaz o en `config.toml`.

### ElevenLabs

Para usar ElevenLabs necesitas:

- `ElevenLabs API Key`
- `ElevenLabs Model ID`
- `ElevenLabs Voice ID` o seleccionar una voz desde la UI si tu cuenta devuelve el listado

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
