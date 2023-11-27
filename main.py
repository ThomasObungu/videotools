from file_manipulation import FileManipulation #Imports classes from different files # Imports file management aspect of files
from ffmpeg_process import FFmpegProcess #Imports the ffmpeg command shortcuts
from commands import Commands #Imports commmands regarding ffmpeg for the console
from console import Console #Imports the actual command line interface to enter the commands into

def main(): # Calling the classes
    FileManipulation()
    FFmpegProcess()
    Commands()
    # Setting varibles for the classes
    console = Console()
    console.run() # Running class through varible

if __name__ == "__main__":
    main()
