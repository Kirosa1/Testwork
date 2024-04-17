from flask import render_template,send_from_directory
import os

macro =[]


def hello_world():
    return "MVC框架!"

def rendering():
    return render_template('index.html')

def download_file(rootpath,filename):
    macro['DOWNLOAD_FOLDER'] = 'download'
    filepath = os.path.join(rootpath, macro['DOWNLOAD_FOLDER'])
    return send_from_directory(filepath,filename,as_attachment=True)