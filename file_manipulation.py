import tkinter
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
