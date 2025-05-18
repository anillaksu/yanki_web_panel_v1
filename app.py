from flask import Flask, render_template, request, jsonify
import os, uuid

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate/scene", methods=["POST"])
def generate():
    text = request.json.get("text", "").strip()
    if not text:
        return jsonify({"error": "Boş metin"}), 400
    sid = f"scene_{uuid.uuid4().hex[:8]}"
    os.makedirs(f"output/{sid}", exist_ok=True)
    open(f"output/{sid}/final_video.mp4", "wb").write(b"")
    return jsonify({"video_url": f"/download/{sid}"})

@app.route("/download/<sid>")
def download(sid):
    return app.send_static_file(f"output/{sid}/final_video.mp4")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
