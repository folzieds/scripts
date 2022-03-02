from os import path
from pydub import AudioSegment

# file path
src = input("In: ")
dest = input("Out: ")

#convert mp3 to wav
sound = AudioSegment.from_mp3(src)
sound.export(dest, format = 'wav')