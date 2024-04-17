from flask import Flask,send_file,request,send_from_directory
import os
from app.route import *
import subprocess
from app import app
    


if __name__ == "__main__":
    app.run(debug=True, port=8000)

@app.route('/app/download/<filename>')
def downloads(filename):
    return download_file(app.root_path,filename)
    #return app.root_path

    

