from file_manipulation import FileManipulation
from ffmpeg_process import FFmpegProcess
from commands import Commands
from console import Console

def main():
    FileManipulation()
    FFmpegProcess()
    Commands()
    
    console = Console()
    console.run()

if __name__ == "__main__":
    main()
