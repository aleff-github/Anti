from moviepy.editor import *

INIT_PATH = "../Anti/separare-video-e-auto-da-un-file-MP4-in-Python/docs"

# Path del file mp4 da cui estrarre audio e video
video_path = INIT_PATH + "/rick.mp4"

# Crea un oggetto VideoFileClip dal file mp4
video = VideoFileClip(video_path)

# Estrae l'audio dal video
audio = video.audio

# Salva l'audio in un file mp3
audio_path = INIT_PATH + "/rick_audio.mp3"
audio.write_audiofile(audio_path)

# Operazione audio completata: Chiudi il file video e audio
video.close()
audio.close()

# Crea un oggetto VideoFileClip dal file mp4 senza audio
video = VideoFileClip(video_path).without_audio()

# Salva il video in un file mp4
video_path = INIT_PATH + "/rick_video.mp4"
video.write_videofile(video_path, codec='libx264')

# Operazione video completata: Chiudi il file video
video.close()