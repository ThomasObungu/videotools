from ffmpeg_process import FFmpegProcess

class Commands(FFmpegProcess):  
    def __init__(self):
        super().__init__()
        self.commands = {
            'comds': self.display_commands,
            'vidtoaud': self.convert_video_to_audio,
            'vidspeedc': self.speed_up_video,
            'vidresc' : self.change_video_res
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
