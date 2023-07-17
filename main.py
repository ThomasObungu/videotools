import pyfiglet
import subprocess
import os
import tkinter
import moviepy.editor as moviepy
from tkinter import filedialog


class FileManipulation:
    def __init__(self):
        self.video_file_types = ("Video files", "*.mp4;*.avi;*.mkv;*.mov;*.m4a")
        self.audio_file_types = ("Audio files", "*.mp3;*.wav;*.ogg")

    def search_for_file(self, filetype):
        tk = tkinter.Tk()
        tk.withdraw()

        filetypes = ()

        if filetype == "video":
            filetypes = (self.video_file_types, ("All files", "*.*"))
        elif filetype == "audio":
            filetypes = (self.audio_file_types,("All files", "*.*"))

        file_path = filedialog.askopenfilename(parent=tk, filetypes=filetypes)
        if len(file_path) > 0:
            print(f"Selected file: {file_path}")
        return file_path


class FFmpegProcess(FileManipulation):
    def __init__(self):
        super().__init__()
        self.audio_directory = os.path.join(os.path.dirname(__file__), 'Audios')
        self.video_directory = os.path.join(os.path.dirname(__file__), 'Videos')

    def convert_video_to_audio(self, **kwargs):
        file = self.search_for_file("video")
        input_file = os.path.abspath(file)
        output_directory = self.audio_directory


        bitrate = int(kwargs.get('bitrate', 192))
        sample_rate = int(kwargs.get('samplerate', 44100))

        ffmpeg_cmd = [
            "ffmpeg",   
            "-loglevel", "quiet",
            "-i", input_file,
            "-vn",
            "-acodec", "libmp3lame",
            "-ab", f"{bitrate}k",
            "-ar", str(sample_rate),
            "-y",
            os.path.join(output_directory, f"{os.path.basename(input_file).split('.')[0]}.mp3")
        ]

        try:
            subprocess.run(ffmpeg_cmd, check=True)
            print("Successfully converted!")
        except subprocess.CalledProcessError as error:
            print("Conversion failed.")
            
    def speed_up_video(self, **kwargs):

        speed = float(kwargs.get('speed', 1))

        file = self.search_for_file("video")
        input_file = os.path.abspath(file)
        output_directory = self.video_directory
        
        ffmpeg_cmd = [
            "ffmpeg",
            "-loglevel", "quiet",
            "-i", input_file,
            "-filter_complex", f'[0:v]setpts={1/speed}*PTS[v];[0:a]atempo={speed}[a]',
            "-map", '[v]',
            "-map", '[a]',
            os.path.join(output_directory, f"{os.path.basename(input_file).split('.')[0]}_{speed}x.mp4")
        ]

        try:
            subprocess.run(ffmpeg_cmd, check=True)
            print("Successfully converted!")
        except subprocess.CalledProcessError as error:
            print("Conversion failed.")

f'()'
class Commands(FFmpegProcess):  
    def __init__(self):
        super().__init__()
        self.commands = {
            'comds': self.display_commands,
            'vidtoaud': self.convert_video_to_audio,
            'vidspeedc': self.speed_up_video
        }

    def display_commands(self):
        commands = [
            'ytomp4 - Youtube to .mp4',
            'yttomp3 - Youtube to .mp3',
            'vidresc - Video resolution & aspect changer',
            'vidspeedc - Video speed changer',
            'vidtoaud - Video(.mp4|.avi|.mkv|.mov|.m4a) to audio(.mp3)',
        ]
        for command in commands:
            print(command)


class Console(Commands):
    def __init__(self):
        super().__init__()
        self.banner = pyfiglet.figlet_format('VideoTools')

    def run(self):
        print(self.banner, flush=True)
        print("Type 'comds' for a list of commands")

        while True:
            menu_choice = input("\n>> ").lower()
            command_parts = menu_choice.split()
            command = command_parts[0]

            if command in self.commands:
                if len(command_parts) > 1:
                    params = {}
                    for arg in command_parts[1:]:
                        key, value = arg.split('=')
                        params[key] = value
                    self.commands[command](**params)
                else:
                    self.commands[command]()
            else:
                print("Invalid command.")

if __name__ == "__main__":
    console = Console()
    console.run()
