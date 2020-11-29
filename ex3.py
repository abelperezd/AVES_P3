# -*- coding: utf-8 -*-
'''
Ref:
    https://stackoverflow.com/questions/1996518/retrieving-the-output-of-subprocess-call
    https://stackoverflow.com/questions/2869281/how-to-determine-video-codec-of-a-file-with-ffmpeg
    https://stackoverflow.com/questions/3271478/check-list-of-words-in-another-string
'''
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
import sys


# Cuando utilizamos el script 4 pasamos el nombre como argumento para hacer el script automático
if sys.argv[1:]:
    inp = sys.argv[1]
else:
    print("Insert the name of the video (extension included): ")
    inp = input()

name = os.path.splitext(inp)[0]  # Extraemos el nombre
ext = os.path.splitext(inp)[1]  # Extraemos la extension

# Extraemos los codecs de audio y de vídeo de todas las pistas
string = 'ffprobe -v error -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 {}'.format(inp)
outp = subprocess.check_output(string, shell=True)
videoCodecs = str(outp)

# Codecs compatibles para cada formato de broadcast
DVBv = ["mpeg2video", "h264"]
DVBa = ["aac", "ac3", "mp3"]

ISDBv = ["mpeg2video", "h264"]
ISDBa = ["aac"]

ATSCv = ["mpeg2video", "h264"]
ATSCa = ["ac3"]

DTMBv = ["avs", "avs+", "mpeg2video", "h264"]  # avs+ no existe
DTMBa = ["dra", "aac", "ac3", "mp2", "mp3"]  # dra no existe

formats = ["DVB", "ISDB", "ATSC", "DTMB"]

acodecs = [DVBa,  ISDBa,  ATSCa,  DTMBa]
vcodecs = [DVBv, ISDBv, ATSCv, DTMBv]
correct_formats = []  # Lista de formatos compatibles

# Para cada formato de broadcast, miramos si en el container tenemos como mínimo un codec de audio y de vídeo
# compatibles
for i in range(len(formats)):
    if any(codec in videoCodecs for codec in vcodecs[i]):
        if any(codec in videoCodecs for codec in acodecs[i]):
            correct_formats.append(formats[i])

if not correct_formats:
    print("ERROR: no broadcast format compatible.")
else:
    print("Compatible broadcast formats: ")
    print(correct_formats)
