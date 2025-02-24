import os
from pytube import YouTube
from colorama import Fore, Style
from os import system
import sys
import time

system("cls||clear")
def rainbow_text(text, delay=0.1):
    colors = [
    "\033[31m", "\033[33m", "\033[32m", "\033[36m", "\033[34m", "\033[35m", "\033[37m",
    ]

    for i in range(len(text)):
        char = text[i]
        color = colors[i % len(colors)]
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write("\033[0m")
    sys.stdout.write("\n")

def main():
    rainbow_text("Coding by xberkay-o")
    sys.stdout.write("\033[37m")
    sys.stdout.write("Coding by xberkay-o\n")
	
if __name__ == "__main__":
    rainbow_text("Coding by xberkay-o")

MENU = """{}
----------- Video Downloader App --------------
{}1. Convert to MP3
{}2. Convert to MP4
{}3. Contact İnfo
{}4. Exit
{}-----------------------------------------------{}
""".format(Fore.LIGHTMAGENTA_EX, Fore.RED, Fore.RED, Fore.GREEN, Fore.LIGHTWHITE_EX, Fore.LIGHTMAGENTA_EX, Fore.RESET)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def convert_to_mp3(video_url, output_folder):
    try:
        yt = YouTube(video_url)

        current_directory = os.getcwd()
        output_path = os.path.join(current_directory, output_folder, f"{yt.title}.mp3")

        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_folder)

        old_file_path = os.path.join(output_folder, audio_stream.default_filename)
        new_file_path = os.path.join(output_folder, f"{yt.title}.mp3")
        os.rename(old_file_path, new_file_path)

        print("Video download and conversion complete:", new_file_path)
    except Exception as e:
        print(f"Hata (URL: {video_url}):", e)

def convert_to_mp4(video_url, output_folder):
    try:
        yt = YouTube(video_url)

        current_directory = os.getcwd()
        output_path = os.path.join(current_directory, output_folder, f"{yt.title}.mp4")

        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_folder)

        print("Video download complete:", output_path)
    except Exception as e:
        print(f"Hata (URL: {video_url}):", e)

def show_contact_info():
    system("cls||clear")
    print("\n--- İ N F O ---")
    print("GitHub: " + Fore.GREEN + "github.com/xberkay-o" + Fore.RESET)

def main():
    input_file = "links.txt"
    mp3_output_folder = "mp3"
    mp4_output_folder = "mp4"

    if not os.path.exists(mp3_output_folder):
        os.makedirs(mp3_output_folder)

    if not os.path.exists(mp4_output_folder):
        os.makedirs(mp4_output_folder)

    while True:
        clear_console()
        print(MENU)
        choice = input("{}Please enter an option (1/2/3/4): ".format(Fore.RED))

        if choice == "1":
            with open(input_file, "r") as file:
                video_urls = file.readlines()

            for url in video_urls:
                url = url.strip()
                if url:
                    convert_to_mp3(url, mp3_output_folder)

        elif choice == "2":
            with open(input_file, "r") as file:
                video_urls = file.readlines()

            for url in video_urls:
                url = url.strip()
                if url:
                    convert_to_mp4(url, mp4_output_folder)

        elif choice == "3":
            show_contact_info()

        elif choice == "4":
            system("cls||clear")
            print("""
 {}Thank you for choosing us.
 {}Exiting...{}
                  """.format(Fore.LIGHTWHITE_EX, Fore.LIGHTRED_EX, Fore.RESET))
            break

        input("\n{}Press Enter to return".format(Fore.GREEN))

if __name__ == "__main__":
    main()
