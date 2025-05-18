import subprocess
import sys

text = sys.argv[1] if len(sys.argv) > 1 else "Yankı aktif!"

subprocess.run(["python", "generate_tts.py", text])
subprocess.run(["python", "generate_image.py", text])
subprocess.run(["python", "generate_subtitle.py", text])
subprocess.run(["python", "generate_video.py"])
