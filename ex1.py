# -*- coding: utf-8 -*-
'''
Ref:
    bit rate: https://superuser.com/questions/319542/how-to-specify-audio-and-video-bitrate
    subtitulos: https://github.com/moust/MediaPlayer/blob/master/demo/subtitles.srt
    container: https://www.youtube.com/watch?v=lE1y_TTISTQ
'''

import subprocess
import os

print("Insert the name of the BBB video (extension included): ")
inp = input()
name = os.path.splitext(inp)[0]  # Extraemos el nombre
ext = os.path.splitext(inp)[1]  # Extraemos la extension

# Recortamos el primer minuto del video
string = 'ffmpeg -i {} -ss 00:00:00 -to 00:01:00 {}1{}'.format(inp, name, ext)
subprocess.call(string, shell=True)

# Extreamos el audio en formato mono en .mp3
string = 'ffmpeg -i {}1{} -ac 1 -vn {}1_mono.mp3'.format(name, ext, name)
subprocess.call(string, shell=True)

# Extraemos el audio con un bit rate de 24k en .mp3
string = 'ffmpeg -i {}1{} -b:a 24k -vn {}1_br.mp3'.format(name, ext, name)
subprocess.call(string, shell=True)

# Generamos subtitulos
string = 'ffmpeg -i subtitles.srt subs.ass'
subprocess.call(string, shell=True)
# Añadimos subtitulos al vídeo
string = 'ffmpeg -i {}1{} -vf "ass=subs.ass" {}1_sub.mp4'.format(name, ext, name)
subprocess.call(string, shell=True)

# Añadimos el vídeo, las pistas de audio y los subtítulos a un unico container
string = 'ffmpeg -i {}1{} -i {}1_mono.mp3 -i {}1_br.mp3 -c copy -map 0:0 -map 0:1 -map 1:0 -map 2:0 -vf "ass=subs.ass" {}1_container.mp4'.format(name, ext, name, name, name)
subprocess.call(string, shell=True)
