import re
import os
from yt_dlp import YoutubeDL

def sanitize_filename(filename):
    # Replace invalid characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def fetch_and_merge():
    # Get YouTube link from user
    link = input("Enter the YouTube link: ")

    try:
        # Fetch available formats
        ydl_opts = {'listformats': True}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=False)

        print("\nAvailable video formats:")
        video_formats = [
            fmt for fmt in info['formats'] if fmt.get('vcodec') != 'none' and fmt.get('acodec') == 'none'
        ]
        for fmt in video_formats:
            size_mb = fmt.get('filesize', 0) / (1024 * 1024)
            print(f"{fmt['format_id']}: {fmt['resolution']} - {size_mb:.2f} MB")

        print("\nAvailable audio formats:")
        audio_formats = [
            fmt for fmt in info['formats'] if fmt.get('acodec') != 'none' and fmt.get('vcodec') == 'none'
        ]
        for fmt in audio_formats:
            size_mb = fmt.get('filesize', 0) / (1024 * 1024)
            print(f"{fmt['format_id']}: {fmt['abr']}kbps - {size_mb:.2f} MB")

        # User selects video format
        video_id = input("\nEnter the format ID for the video: ")

        # User selects audio format
        audio_id = input("Enter the format ID for the audio: ")

        # Define download options for video
        video_path = None
        ydl_opts = {
            'format': video_id,
            'outtmpl': '%(title)s_video.%(ext)s'  # Template for video filename
        }
        print("\nDownloading video...")
        with YoutubeDL(ydl_opts) as ydl:
            video_info = ydl.extract_info(link)
            video_path = ydl.prepare_filename(video_info)

        # Define download options for audio
        audio_path = None
        ydl_opts = {
            'format': audio_id,
            'outtmpl': '%(title)s_audio.%(ext)s'  # Template for audio filename
        }
        print("Downloading audio...")
        with YoutubeDL(ydl_opts) as ydl:
            audio_info = ydl.extract_info(link)
            audio_path = ydl.prepare_filename(audio_info)

        # Ensure both files exist
        if not os.path.exists(video_path) or not os.path.exists(audio_path):
            raise FileNotFoundError("Video or audio file not found after download.")

        # Sanitize the title for the output file
        title = sanitize_filename(video_info['title'])
        output_file = f"{title}_output.mp4"

        # Merge video and audio using FFmpeg
        print("\nMerging video and audio...")
        os.system(f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v copy -c:a aac "{output_file}"')

        # Cleanup temporary files
        os.remove(video_path)
        os.remove(audio_path)

        print(f"\nDownload and merge completed! File saved as {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    fetch_and_merge()
