#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
# import save_file as gen
# import work as gen
import os
# import run.static.work as load_
from static.python.work import img


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')
    
@app.route('/run', methods=['GET', 'POST'])
def parse_data():
    # gen.main()
    # load_.main()
    img()
    return "Run"

# if __name__ == '__main__':
app.run(host='0.0.0.0', port=8080, debug=True)
