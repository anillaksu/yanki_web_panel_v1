import sys

def generate_subs(text, output_path="static/subtitles.srt"):
    with open(output_path, "w") as f:
        f.write("1\n")
        f.write("00:00:00,000 --> 00:00:04,000\n")
        f.write(text + "\n")

if __name__ == "__main__":
    generate_subs(sys.argv[1] if len(sys.argv) > 1 else "Yankı konuşuyor.")
