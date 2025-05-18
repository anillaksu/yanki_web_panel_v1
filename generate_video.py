from moviepy.editor import *

img_clip = ImageClip("static/output.png").set_duration(4)
audio_clip = AudioFileClip("static/output.wav")
final = img_clip.set_audio(audio_clip)
final.write_videofile("static/output.mp4", fps=24)
