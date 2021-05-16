from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, request
import json
import toonify
import lipsync
import os
import shutil
import threading
import gc
from numba import cuda

app = Flask(__name__)
run_with_ngrok(app)

NUM_ITERS = 500

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/generate', methods = ['GET', 'POST'])
def generate():
    if request.method == 'POST':
        f = request.files['file']
        f.save('static/uploads/input.png')
        with open('static/uploads/input.json', 'w') as fp:
            json.dump(request.form, fp)

        toon_talk()

        return render_template('result.html')

    return render_template('index.html')

def toon_talk():
    global NUM_ITERS
    
    # Reset Files
    if os.path.isdir('raw/'):
        shutil.rmtree('raw/')

    if os.path.isdir('aligned/'):
        shutil.rmtree('aligned/')

    if os.path.isdir('generated/'):
        shutil.rmtree('generated/')
        
    try:
        os.mkdir('raw/')
        os.mkdir('aligned/')
        os.mkdir('generated/')
    except:
        pass

    shutil.move('static/uploads/input.png', 'raw/input.png')
    toonify.run(NUM_ITERS)
    shutil.move('generated/input_01-toon.jpg', 'static/uploads/input_01-toon.jpg')
    
    lipsync.run()

def create_app(iters):
    global NUM_ITERS
    NUM_ITERS = iters
    return app

