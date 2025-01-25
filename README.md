# YouTube Video and Audio Downloader with Merge

## Overview
This project is a Python-based tool that allows users to:
1. Download video and audio streams from YouTube.
2. Merge the downloaded video and audio into a single file using FFmpeg.

The script leverages the `yt_dlp` library for downloading media and uses FFmpeg for merging video and audio streams.

## Features
- List available video and audio formats for a given YouTube link.
- Download video and audio streams separately.
- Automatically merge the downloaded files into a single MP4 file.
- Sanitize filenames to avoid invalid characters.

## Prerequisites
Before running this script, ensure the following dependencies are installed on your system:

1. **Python**: Install Python (3.6 or higher).
2. **yt_dlp**: Install the `yt_dlp` library by running:
   ```bash
   pip install yt-dlp
   ```
3. **FFmpeg**: Install FFmpeg on your system. For installation instructions, visit the [FFmpeg website](https://ffmpeg.org/).

## Usage
1. Clone the repository or download the script.
2. Run the script using Python:
   ```bash
   python app.py
   ```
3. Enter the YouTube link when prompted.
4. Select the desired video and audio formats from the displayed list.
5. The script will download the selected formats and merge them into a single MP4 file.

## Code Explanation
### Key Functions:
- **`sanitize_filename`**: Replaces invalid characters in filenames with underscores.
- **`fetch_and_merge`**: Main function that:
  - Fetches available formats from a YouTube link.
  - Allows the user to select video and audio formats.
  - Downloads the selected formats.
  - Merges video and audio files using FFmpeg.
  - Cleans up temporary files after merging.

### Error Handling:
- The script includes error handling to manage issues like:
  - Invalid YouTube links.
  - Missing dependencies (e.g., FFmpeg).
  - Download or merge failures.

## Example Output
```bash
Enter the YouTube link: https://www.youtube.com/watch?v=example

Available video formats:
18: 360p - 20.00 MB
22: 720p - 50.00 MB

Available audio formats:
140: 128kbps - 5.00 MB
251: 160kbps - 6.00 MB

Enter the format ID for the video: 22
Enter the format ID for the audio: 140

Downloading video...
Downloading audio...

Merging video and audio...

Download and merge completed! File saved as Example_Title_output.mp4
```

## License
This project is licensed under the MIT License.

## Acknowledgments
- [yt_dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)

## Support
If you find this project helpful, consider supporting me at [Buy Me a Coffee](https://buymeacoffee.com/justnative).

