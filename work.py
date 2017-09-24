#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import ImageFont, Image, ImageDraw


def generate_image(in_img, out_img, text, pos, color, text_size):
    img = Image.open(in_img)

    font = ImageFont.truetype(font='10262.otf', size=text_size)
    draw = ImageDraw.Draw(img)

    draw.text(pos, text, color, font=font)
    draw = ImageDraw.Draw(img)

    img.save(out_img)


def img(house, my_arr):
    # text_arr = ["1.5%", "20 °C", "26 °C", "<1200", "162", "25%", "<440", "<20", "10%", "40%", "65%", "10%"]
    # text_arr = ["1.5%", "20 °C", "22 °C", "<1200", "162", "25%", "<440", "<20", "10%", "40%", "65%", "10%"]
    text_arr = my_arr
    positions = [(445, 493), (681, 380), (798, 380), (1090, 507), (1200, 720),
        (1085, 1065), (925, 1260), (620, 1195), (353, 993), (325, 910),
        (325, 850), (325, 785)]

    text_color = (100, 100, 100)
    text_size = 20
    in_img = 'radar.png'
    out_img = 'static/img/house' + house + '.png'

    for i in range(len(text_arr)):
        text = text_arr[i]
        position = positions[i]
        generate_image(in_img, out_img, text, position, text_color, text_size)
        in_img = out_img
