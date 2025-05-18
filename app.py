from flask import Flask, render_template, request, jsonify
import subprocess, uuid, os

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate/scene", methods=["POST"])
def generate():
    data = request.get_json()
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "Metin boş olamaz"}), 400

    sid = f"scene_{uuid.uuid4().hex[:8]}"
    output_dir = os.path.join("static", sid)
    os.makedirs(output_dir, exist_ok=True)

    try:
        subprocess.run(["python", "auto_generate_all.py", text], check=True)
        for fname in ["output.png", "output.wav", "subtitles.srt", "output.mp4"]:
            src = os.path.join("static", fname)
            dst = os.path.join(output_dir, fname)
            if os.path.exists(src):
                os.rename(src, dst)
        return jsonify({"video_url": f"/static/{sid}/output.mp4"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
