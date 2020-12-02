# -*- coding: utf-8 -*-

'''
DVB:
    *Video: MPEG2, h.264
    *Audio: AAC, Dolby Digital (AC-3), mp3
ISDB:
    *Video: MPEG2, h.264
    *Audio: AAC
ATSC:
    *Video: MPEG2, h.264
    *Audio: AC-3
DTMB:
    *Video: AVS, AVS+, MPEG2, h.264
    *Audio: DRA, AAC, AC-3, MP2, MP3
'''


import subprocess
import os

print("Insert the number of files you want to add: ")
nfiles = input()

files = []
channels = []

# Obtenemos el nombre de los archivos y cuántos canales tiene cada uno
print("Insert the name of the files and its number of channels (extension included): ")
for i in range(int(nfiles)):
    print("File " + str(i+1) + ":")
    inp = input()
    files.append(inp)
    print("Channels:")
    inp = input()
    channels.append(inp)

# Generamos el comando
string = "ffmpeg "

# Añadimos al string el nombre de todos los archivos
for i in range(int(nfiles)):
    string = string + "-i {} ".format(files[i])

# Para conservar los codecs
string = string + "-c copy "

# Añadimos los canales para cada archivo
for i in range(int(nfiles)):
    for j in range(int(channels[i])):
        string = string + "-map {}:{} ".format(i, j)

# Añadimos el nombre final del container
string = str(string + "container.mp4")
print(string)

subprocess.call(string, shell=True)
