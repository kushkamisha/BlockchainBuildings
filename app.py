#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import work
import time


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')
    
@app.route('/house1', methods=['GET', 'POST'])
def generate_house1():
    arr = ["1.5%", "20 C", "26 C", "<1200", "162", "25%", "<440", "<20", "10%", "40%", "65%", "10%"]
    tm = str(round(time.time()))
    work.img(tm, arr, '1')
    return tm
    
@app.route('/house2', methods=['GET', 'POST'])
def generate_house2():
    arr = ['4%', '21 C', '24 C', '<900', '58', '60%', '<150', '<7', '25%', '50%', '80%', '30%']
    tm = str(round(time.time()))
    work.img(tm, arr, '2')
    return tm
    
@app.route('/house3', methods=['GET', 'POST'])
def generate_house3():
    arr = ['6%', '21 C', '24 C', '<750', '45', '80%', '<28', '<5', '40%', '90%', '90%', '40%']
    tm = str(round(time.time()))
    work.img(tm, arr, '3')
    return tm

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)#, debug=True)
