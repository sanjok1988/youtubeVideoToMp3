from pytube import YouTube
import moviepy.editor as mp
import os
import re

def extract_audio(url):
    try:
        download_path='/Users/sanjokdangol/Projects/python/youtubeToMp3/downloads'
        # Ensure the output folder exists, create if not
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first().download(download_path)
        
    except Exception as e:
        print(f"Error downloading audio from {url}: {str(e)}")

def process_youtube_links(file_path='youtube_links.txt'):
    with open(file_path, 'r') as file:
        youtube_links = file.read().splitlines()

    for link in youtube_links:
        extract_audio(link)
        print()

    folder='/Users/sanjokdangol/Projects/python/youtubeToMp3/downloads'
    for file in os.listdir(folder):
        if re.search('mp4', file):
            mp4_path = os.path.join(folder,file)
            print(mp4_path)
            mp3_path = os.path.join(folder+'/../output/',os.path.splitext(file)[0]+'.mp3')
            print(mp3_path)
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)

    print(f"Audio downloaded successfully")

def main():
    process_youtube_links()

if __name__ == "__main__":
    main()
