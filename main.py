import  pyfiglet, subprocess, os, tkinter, re
import moviepy.editor as moviepy
from tkinter import filedialog

#Functions

def search_for_video_file():

    tk = tkinter.Tk()
    tk.withdraw()

    filetypes = (
        ("Video files", "*.mp4;*.avi;*.mkv;*.mov;*.m4a"),
        ("All files", "*.*")
    )
    file_path = filedialog.askopenfilename(parent=tk, filetypes=filetypes)
    if len(file_path) > 0:
        print(f"Selected file : {file_path}")
    return file_path

def convert_video_to_mp3(input_file, bitrate, sample_rate):
    input_file = os.path.abspath(input_file)
    output_directory = os.path.join(os.path.dirname(__file__), 'Audios')

    ffmpeg_cmd = [
        
        "ffmpeg",
        "-loglevel", "quiet",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", str(f'{bitrate}k'),
        "-ar", str(sample_rate),
        "-y",
        os.path.join(output_directory, f'{"".join(re.split(r".mp4|.avi|.mkv|.mov|.m4a","".join(os.path.basename(input_file))))}.mp3')
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Successfully converted!")

    except subprocess.CalledProcessError as error:
        print("Conversion failed.")


def convert_to_mp4(input_file):
    input_file = os.path.abspath(input_file)

    file = moviepy.VideoFileClip(input_file)
    file.write_videofile(f'{os.path.basename(input_file)}.mp4')


print(f"{pyfiglet.figlet_format('VideoTools')}", flush=True)

#Commands 

commands = [
    'ytomp4 - Youtube to .mp4',
    'yttomp3 - Youtube to .mp3',
    'vidresc - Video resolution & aspect changer',
    'vidspeedc - Video speed changer',
    'vidtoaud - Video(.mp4|.avi|.mkv|.mov|.m4a) to aduio(.mp3)',
    ]

def comds():
    for i in commands:
        print(i)
    

def vidtoaud(bitrate, samplerate):
    file = search_for_video_file()
    convert_video_to_mp3(file, bitrate, samplerate)

# Command line 

def  menu():

    choices={
    'comds' : comds,
    'vidtoaud' : vidtoaud,
    }

    print("Type comds for a list of commands")
    
    while True:

        menu_choice=(input("\n>> ")).lower()
        seperators=[","," ",]
        command=re.split('|'.join(map(re.escape,seperators)), menu_choice)
        command=[i for i in command if i != '']

        bitrate=192
        samplerate=44100

        if command[0] in choices and len(command) > 1:
            if command[0] == 'vidtoaud':
                for i in command[1:]:
                    i_name, i_value = i.split('=')
                    if i_name == 'bitrate':
                        bitrate = int(i_value)
                    elif i_name == 'samplerate':
                        samplerate = int(i_value)
                choices[command[0]](bitrate,samplerate)
                continue
        else:
            choices[command[0]](bitrate,samplerate)
            continue
        
        choices[menu_choice]()

menu()





        
    
