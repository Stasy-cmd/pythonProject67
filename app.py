from flask import Flask, request, render_template, send_from_directory
# from functions import ...
from lesson12_project_source_v3.loader.views_loader import loader_blueprint
from lesson12_project_source_v3.main.views_main import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

app.run()

