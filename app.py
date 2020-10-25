from flask import Flask, render_template
from benford import detect_benford
import json

app = Flask(__name__)
UPLOAD_FOLDER = '/var/www/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            return filepath
            resp = detect_benford(filepath)
            # file.save(filepath)

            return redirect(url_for('answer',
                                    analisys=json.dumps(resp)))
    return render_template('index.html')


@app.route('/answer', methods=['GET', 'POST'])
def answer():
    resp = {}
    try:
        resp = json.loads(str(request.args.get("analisys")))
    except:
        return "error loading get args"

    color_palette = ["rgba(255, 241, 0, 0.2)", "rgba(255, 140, 0, 0.2)", "rgba(232, 17, 35, 0.2)",
                     "rgba(0, 158, 73, 0.2)", "rgba(186, 216, 10, 0.2)",
                     "rgba(0, 24, 143, 0.2)", "rgba(0, 188, 242, 0.2)", "rgba(0, 178, 148, 0.2)",
                     "rgba(236, 0, 140, 0.2)", "rgba(104, 33, 122, 0.2)"
                     ]

    if len(color_palette) < len(resp["columns_distribution"]):
        return "to many columns to display"

    return render_template("answer.html", resp=resp, cols_len=len(resp["columns_distribution"]), color_palette=color_palette)


if __name__ == '__main__':
    app.run()






