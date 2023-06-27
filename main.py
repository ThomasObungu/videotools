import  pyfiglet, subprocess, os, tkinter, re
from tkinter import filedialog

#Functions

def search_for_video_file():

    tk = tkinter.Tk()
    tk.withdraw()

    filetypes = (
        ("Video files", "*.mp4;*.avi;*.mkv;*.mov;*.m4a;*.3gp;*.3g2;*.mj2;*"),
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
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", bitrate,
        "-ar", sample_rate,
        "-y",
        os.path.join(output_directory, f'{"".join(re.split(r".mp4|.avi|.mkv|.mov|.m4a|.3gp|3g2|mj2","".join(os.path.basename(input_file))))}.mp3')
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Successfully converted!")
        input("Press any key to exit...")
    except subprocess.CalledProcessError as error:
        print("Conversion failed.")
        input("Press any key to exit...")

print(f"{pyfiglet.figlet_format('VideoTools')}", flush=True)

#Commands 

def comds():
    for i in commands:
        print(i)

def vidtoaud():
    file = search_for_video_file()
    convert_video_to_mp3(file, '192k', '44100')

commands = [
    'ytomp4 - Youtube to .mp4',
    'yttomp3 - Youtube to .mp3',
    'vidresc - Video resolution & aspect changer',
    'vidspeedc - Video speed changer',
    'vidtoaud - Video(.mp4|.avi|.mkv|.mov|.m4a|.3gp|3g2|mj2) to aduio(.mp3)',
    ]

menu_choice=(input("Type comds for a list of commands \n\n>> "))

choices={
    'comds' : comds,
    'vidtoaud' : vidtoaud,
    }

choices[menu_choice]()



        
    
