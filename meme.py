#!/usr/bin/env python3
import json
import sys
from PIL import ImageDraw, Image, ImageFont

with open("memes.json") as f:
    memes = json.load(f)
    memes_by_id = {}
    for filename, meme in memes.items():
        meme["filename"] = filename
        memes_by_id[meme["identifier"]] = meme

def create_meme(font_path, meme_id, *texts, filepath):
    meme = memes_by_id[meme_id]
    img = Image.open("images/" + meme["filename"])
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, 16)
    text_points = meme["text_points"]
    assert len(texts) == len(text_points), f"number of points required {len(text_points)} does not match up with the number of text inputs provided, please give the exact number of text inputs"

    for text, point in zip(texts, text_points):
        fill = (0, 0, 0)
        tb = draw.textbbox(point, text, font=font, anchor="ms")
        draw.rectangle(tb, "white")
        draw.text(point, text, fill, anchor="ms", font=font)
        img.save(filepath)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("usage: ./meme.py <meme-name> <text-1> <text-2> ... <file_name>")
        print("where <meme-name> is one of")
        print([*memes_by_id.keys()])
    else:
        font_path = "./fonts/Roboto/Roboto-Regular.ttf"
        create_meme(font_path, sys.argv[1], *sys.argv[2:-1], filepath=sys.argv[-1])