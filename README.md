# yt_mp3

A small Python utility that downloads audio from YouTube videos, converts it to MP3, and embeds the video's title and thumbnail into the MP3 file as ID3 metadata (title and cover art).

This repository contains a single script, `yt_mp3.py`, which uses `yt-dlp` to fetch video audio and `mutagen` to write ID3 tags. It prompts for a YouTube URL and an optional output folder (defaults to `downloads`).

## Features

- Downloads the best available audio and converts it to MP3 using ffmpeg
- Embeds the video title as the ID3 title tag
- Embeds the video's thumbnail as album art (APIC)
- Creates the output folder automatically
- Simple interactive CLI

## Requirements

- Python 3.8+
- ffmpeg (must be installed and available on PATH)
- Python packages:
  - `yt-dlp`
  - `mutagen`
  - `requests`

Install the Python packages with pip:

```powershell
pip install yt-dlp mutagen requests
```

Install ffmpeg:

- Windows: download a static build from https://ffmpeg.org/download.html and add `ffmpeg.exe` to your PATH
- macOS: `brew install ffmpeg`
- Debian/Ubuntu: `sudo apt install ffmpeg`

## Usage

Run the script and follow the prompts:

```powershell
python yt_mp3.py
```

When prompted, paste a YouTube URL and optionally enter an output folder. If you leave the folder blank, files will be saved to a `downloads` directory in the repository.

Example (programmatic use):

```python
from yt_mp3 import download_youtube_audio

mp3_path = download_youtube_audio(
    "https://www.youtube.com/watch?v=VIDEO_ID",
    output_path="my_music"
)
print(mp3_path)
```

## Notes and Caveats

- This script relies on `ffmpeg` to perform audio extraction and conversion. If `yt-dlp` cannot find `ffmpeg` on PATH it will fail.
- The generated MP3 filename is based on the video title. Characters invalid for filenames on some platforms may cause errors; consider sanitizing titles if you process many videos programmatically.
- The script downloads the thumbnail URL provided by the extractor and embeds it as `image/jpeg`. If the thumbnail is another format (e.g., PNG), embedding may still work but the mime type is currently fixed to `image/jpeg` in the script.
- Network errors or removed videos will cause the downloader to fail; the script prints errors to stdout.

## License

This repository has no explicit license. If you plan to redistribute or use this project in other projects, add a license file (for example `LICENSE` with an MIT or Apache 2.0 license).

## Contributing

Small fixes and improvements are welcome. Consider adding:

- Better filename sanitization
- CLI flags (URL and output path) so the script can be used non-interactively
- Support for more metadata (artist, album, year) if available from the extractor

---

If you'd like, I can add a more robust CLI (argparse) and a `requirements.txt` or `pyproject.toml`. Which would you prefer?
