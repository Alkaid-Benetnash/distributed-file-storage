#!/usr/bin/python -O
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

import os,sys
import pathlib

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

Bootstrap(app)

@app.route('/list')
def list_dir():
    if request.args.get('local_path'):
        div=0
        arg = request.args.get('local_path')
        path = pathlib.Path(arg)
        filelist=[('..',str(path.parent),0)]
        for f in path.iterdir():
            if f.is_dir():
                filelist.append((f.name,str(f),0))
            else:
                filelist.append((f.name,str(f),1))
    elif request.args.get('remote_path'):
        div=1
        arg = request.args.get('remote_path')
        path = pathlib.Path(arg)
        filelist=[('..',str(path.parent),0)]
        for f in path.iterdir():
            if f.is_dir():
                filelist.append((f.name,str(f),0))
            else:
                filelist.append((f.name,str(f),1))
    filelist.sort(key=lambda f:(f[2],f[0]))
    return render_template('viewfiles.html',curr_path=str(path),filelist=filelist,div=div)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)

