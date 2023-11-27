import tkinter # Imports libaries, tkinter needed for opening and closing files
from tkinter import filedialog # Imports the filedialog aspect from tkinter

class FileManipulation: # Declaring class name
    def __init__(self):  # Initializes class
        self.video_file_types = ("Video files", "*.mp4;*.avi;*.mkv;*.mov;*.m4a") # Specifies the specific video and audio file types allowed, prevents opening of any other files other specified
        self.audio_file_types = ("Audio files", "*.mp3;*.wav;*.ogg") 

    def search_for_file(self, filetype): #Opens windows explorer window to search for file
        tk = tkinter.Tk() # Initializes Tkinter as tk
        tk.withdraw() # Withdraws the small white box made due to intializing tkinter

        filetypes = () # Creates an empty tuple for files types

        if filetype == "video": # If filetype is input as "video" when using the class then filetypes are set to videofile types
            filetypes = (self.video_file_types, ("All files", "*.*")) # These will be shown on the drop down when selecting and opening files
        elif filetype == "audio": # If filetype is input as "audio" when using the class then files are set to audiofile types
            filetypes = (self.audio_file_types,("All files", "*.*")) # 
            # E.g *.* All files, .mp4, .avi... Only allows video files. Not image file

        file_path = filedialog.askopenfilename(parent=tk, filetypes=filetypes) # Opens the path of the file and sets the speicfied filestypes
        if len(file_path) > 0: # If there is a valid name of a file found then it prints out the specified path of file
            print(f"Selected file: {file_path}")
        return file_path # Returna filepath to be used as a path when using ffmpeg commands 
