
# videotools
Simple command line interface program that allows audio and video file manipulation. Made using Python 3 but utilizes the power of FFmepg.
FFmpeg needed to use and Pyfiglet needed to be installed. 
# Instructions
1. Go to releases and download the source code.zip
2. Extract the zip and ensure the dependancies are downloaded and the Audio and Video Folders are in place
3. Run main.py
#
# Dependencies
Python 3.8+

``pip install pyfiglet``

FFmpeg
#
Learn how to install FFmpeg here : https://www.wikihow.com/Install-FFmpeg-on-Windows
#
# Commands
1. **vidresc res=``RESOLUTION e.g. 64``** -> Allows changing of video reslution but in square format e.g resolution of 256 would result in 256x256 video
2. **vidspeedc speed=``SPEED e.g. 1.5``** -> Allows changing of video speed
3. **vidtoaud bitrate=``BITRATE e.g. 32`` samplerate=``SAMPLERATE e.g 220500``** -> Converts video to an .mp3 audio format. Allows the dynamic bitrate and sample rate. Default samplerate and bitrate is 192k and 44100hz
#

![image](https://github.com/Tawitg/videotools/assets/108408219/4e89da57-3721-4e31-9b65-82082a0a9b92)


