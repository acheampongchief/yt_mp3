# There is a problem with youtube or something i don't know about it; probably from yt blocking access or something else
import yt_dlp
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, APIC
import requests
import os

def download_youtube_audio(url, output_path="downloads"):
    """
    Downloads audio from YouTube video and embeds thumbnail and title.
    
    Args:
        url: YouTube video URL
        output_path: Directory to save the MP3 file
    """
    
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
    }
    
    try:
        # Download audio and get video info
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Fetching video information...")
            info = ydl.extract_info(url, download=True)
            
            title = info.get('title', 'Unknown')
            thumbnail_url = info.get('thumbnail', '')
            
            # Construct the output filename
            mp3_filename = os.path.join(output_path, f"{title}.mp3")
            
            print(f"\nTitle: {title}")
            print(f"Downloaded to: {mp3_filename}")
            
            # Download thumbnail
            if thumbnail_url:
                print(f"Downloading thumbnail...")
                thumbnail_data = requests.get(thumbnail_url).content
                
                # Embed metadata
                print(f"Embedding metadata...")
                audio = MP3(mp3_filename, ID3=ID3)
                
                # Add ID3 tags if they don't exist
                try:
                    audio.add_tags()
                except:
                    pass
                
                # Add title
                audio.tags.add(TIT2(encoding=3, text=title))
                
                # Add thumbnail as album art
                audio.tags.add(
                    APIC(
                        encoding=3,
                        mime='image/jpeg',
                        type=3,  # Cover (front)
                        desc='Cover',
                        data=thumbnail_data
                    )
                )
                
                audio.save()
                print(f"✓ Successfully added title and thumbnail to MP3!")
            
            return mp3_filename
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    print("YouTube Audio Downloader")
    print("=" * 50)
    
    # Get URL from user
    url = input("\nEnter YouTube URL: ").strip()
    
    if not url:
        print("Error: No URL provided")
        return
    
    # Optional: custom output path
    custom_path = input("Enter output folder (press Enter for 'downloads'): ").strip()
    output_path = custom_path if custom_path else "downloads"
    
    print(f"\nStarting download...\n")
    result = download_youtube_audio(url, output_path)
    
    if result:
        print(f"\n{'=' * 50}")
        print(f"✓ Download complete!")
        print(f"File saved: {result}")
    else:
        print("\n✗ Download failed")

if __name__ == "__main__":
    main()

''' 
I'll create a Python script that downloads audio from YouTube videos and embeds the thumbnail and title into the MP3 file.I've created a Python script that downloads audio from YouTube videos and embeds both the thumbnail and title into the MP3 file.

## Required Dependencies

Install these packages first:

```bash
pip install yt-dlp mutagen requests
```

You'll also need **FFmpeg** installed on your system:
- **Windows**: Download from ffmpeg.org
- **Mac**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`

## Features

- Downloads highest quality audio and converts to MP3
- Embeds video title as ID3 metadata
- Embeds thumbnail as album art
- Creates a "downloads" folder automatically
- Interactive prompts for URL and output location

## Usage

Run the script and paste your YouTube URL when prompted:

```bash
python script.py
```

Or modify the `main()` function to use URLs directly:

```python
download_youtube_audio("https://www.youtube.com/watch?v=VIDEO_ID", "my_music")
```

The MP3 file will have the title and thumbnail embedded, so they'll show up in music players!'''    