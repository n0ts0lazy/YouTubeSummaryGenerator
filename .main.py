import os
from pytube import YouTube
from dirCheck import createFolders

# Function to download the audio
def download_audio(youtube_url):
    # Create 'Audio cache' folder if it doesn't exist
    createFolders()

    # Create a YouTube object
    yt = YouTube(youtube_url)

    # Get the best audio stream (highest quality)
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Get the video title
    video_title = yt.title

if __name__ == "__main__":
    # Prompt the user for the YouTube URL
    youtube_url = input("Enter the YouTube URL: ")

    # Call the download_audio function
    download_audio(youtube_url)
