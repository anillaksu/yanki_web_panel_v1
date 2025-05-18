import subprocess
import sys

def generate_tts(text, output_path="static/output.wav"):
    subprocess.run([
        "piper",
        "--model", "tr_TR-fahrettin-medium.onnx",
        "--output_file", output_path,
        "--text", text
    ], check=True)

if __name__ == "__main__":
    text = sys.argv[1] if len(sys.argv) > 1 else "Yankı burada!"
    generate_tts(text)
