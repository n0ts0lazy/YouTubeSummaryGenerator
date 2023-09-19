import os
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

from dirCheck import createFolders

# Function to download the video, audio, and transcript
def download_video_audio_and_transcript(youtube_url):
    # Create 'Video cache', 'Audio Cache', and 'Result' folders if they don't exist
    createFolders()

    # Create a YouTube object
    yt = YouTube(youtube_url)

    # Get the highest quality streams for video and audio
    video_stream = yt.streams.get_highest_resolution()
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Get the video title and author for reference
    video_title = yt.title
    video_author = yt.author

    # Get the video ID
    video_id = yt.video_id

    # Set the file path for the downloaded video in 'Video Cache' folder
    print('Downloading video', video_title)
    video_cache_folder = 'Video Cache'

    # Set the file path for the downloaded audio in 'Audio Cache' folder
    print('Downloading audio', video_title)
    audio_cache_folder = 'Audio Cache'

    # Download the video and audio to their respective folders
    video_stream.download(output_path=video_cache_folder)
    audio_stream.download(output_path=audio_cache_folder)

    # Get the transcript using the YouTubeTranscriptApi
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Set the file path for the transcript file in 'Result' folder
    print('Downloading transcript', video_title)
    result_folder = 'Result'
    transcript_file = os.path.join(result_folder, f"{video_title}_transcript.txt")

    # Create a text file for the transcript in the 'Result' folder
    with open(transcript_file, "w", encoding="utf-8") as file:
        file.write(f"Video Title: {video_title}\n")
        file.write(f"Video Author: {video_author}\n\n")
        for entry in transcript:
            text = entry['text']
            file.write(text + "\n")


if __name__ == "__main__":
    # Prompt the user for the YouTube URL
    youtube_url = input("Enter the YouTube URL: ")

    # Call the download_video_audio_and_transcript function
    download_video_audio_and_transcript(youtube_url)
