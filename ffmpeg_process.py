import os
import subprocess
from file_manipulation import FileManipulation

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

    def change_video_res(self, **kwargs):
        
        resolution = float(kwargs.get('res', 1))

        file = self.search_for_file("video")
        input_file = os.path.abspath(file)
        output_directory = self.video_directory
        
        ffmpeg_cmd = [
            "ffmpeg",
            "-loglevel", "quiet",
            "-y", "-i", input_file, "-vf",
            f"scale={resolution}:-2,setsar=1:1", "-c:v", "libx264", 
            "-c:a", "copy",
            os.path.join(output_directory, f"{os.path.basename(input_file).split('.')[0]}_{resolution}x{resolution}.mp4")
        ]

        try:
            subprocess.run(ffmpeg_cmd, check=True)
            print("Successfully converted!")
        except subprocess.CalledProcessError as error:
            print("Conversion failed.")
