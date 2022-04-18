from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def vid():
    return render_template('test_vid.html', video_to_show="/static/fight_small.mp4")
