from PIL import Image, ImageDraw
import sys

def generate_image(text, output_path="static/output.png"):
    img = Image.new("RGB", (720, 1280), color=(15, 15, 15))
    draw = ImageDraw.Draw(img)
    draw.text((50, 600), text, fill=(255, 255, 255))
    img.save(output_path)

if __name__ == "__main__":
    generate_image(sys.argv[1] if len(sys.argv) > 1 else "Yankı sahnede.")
