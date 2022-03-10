import os
from pydub import AudioSegment

# file path
src = "test.mp3"
dest = "test.wav"

#convert mp3 to wav
sound = AudioSegment.from_mp3(src)
sound.export(dest, format = 'wav')