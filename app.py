from flask import Flask, render_template, url_for, request, redirect, make_response, Response
import app
import random
import json
import time

global app
app = Flask(__name__)

@app.route('/chart-data')
def ajax() :
    print("hello we are starting!")
    def ff():
        while True:
            motifs = random.randint(3, 19)
            time.sleep(1)
            json_data = json.dumps({'x': motifs})
            yield f"data:{json_data}\n\n"
    return Response(ff(), mimetype='text/event-stream')

@app.route("/")
def index():
     return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)