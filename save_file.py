#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import ImageFont, Image, ImageDraw

text_arr = ["1.5%", "20 ºC", "26 ºC", "<1200", "162", "25%", "<440", "<20", "10%", "40%", "65%", "10%"]
def generate_image(in_img, out_img, text, pos, color, text_size):
    img = Image.open(in_img)
    font = ImageFont.truetype(font='10262.otf', size=text_size)
    draw = ImageDraw.Draw(img)

    draw.text(pos, text, color, font=font)
    draw = ImageDraw.Draw(img)

    img.save(out_img)
    

def savv():
    with open ("test.txt", 'w') as outfile:
        outfile.write("Succeeded")