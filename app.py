#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import work


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')
    
@app.route('/house1', methods=['GET', 'POST'])
def generate_house1():
    arr = ["100", "20C", "22C", "<1200", "162", "25%", "<440", "<20", "10%", "40%", "65%", "10%"]
    work.img('1', arr)
    return "House1"
    
@app.route('/house2', methods=['GET', 'POST'])
def generate_house2():
    arr = ["100", "20C", "22C", "<1200", "162", "25%", "<440", "<20", "10%", "40%", "65%", "10%"]
    work.img('2', arr)
    return "House2"
    
@app.route('/house3', methods=['GET', 'POST'])
def generate_house3():
    arr = ["", "", "", "", "", "", "", "", "", "", "", ""]
    work.img('3', arr)
    return "House3"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)#, debug=True)
