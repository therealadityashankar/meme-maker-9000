#!/usr/bin/env python3
import sys
import yaml
import os
from PIL import ImageDraw, Image, ImageFont

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
with open(CURR_DIR + "/memes.yaml") as f:
    memes = yaml.safe_load(f)
    memes_by_id = {}
    for filename, meme in memes.items():
        meme["filename"] = filename
        memes_by_id[meme["identifier"]] = meme

font_path = CURR_DIR + "/fonts/Roboto/Roboto-Regular.ttf"

def create_meme(meme_id, texts, filepath):
    meme = memes_by_id[meme_id]
    img = Image.open(CURR_DIR + "/images/" + meme["filename"])
    draw = ImageDraw.Draw(img)
    font_size = 25

    if "font_size" in meme: font_size = meme["font_size"]

    font = ImageFont.truetype(font_path, font_size)
    text_points = meme["text_points"]
    assert len(texts) == len(text_points), f"number of points required {len(text_points)} does not match up with the number of text inputs provided, please give the exact number of text inputs"
    char_limits = [35]*len(text_points)

    if "char_limits" in meme:
        char_limits = meme["char_limits"]

    for text, point, max_chars_per_line in zip(texts, text_points, char_limits):
        fill = (0, 0, 0)
        broken_text = text_refine(text, max_chars_per_line)
        tb = draw.multiline_textbbox(point, broken_text, font=font, anchor="mm")
        draw.rectangle(tb, "white")
        draw.multiline_text(point, broken_text, fill, anchor="mm", font=font)
        img.save(filepath)

def text_refine(text, max_char_len):
    words = text.split(" ")
    final_text = ""
    curr_line = ""
    for word in words:
        if len(curr_line + ' ' + word) > max_char_len:
            final_text += curr_line + "\n"
            curr_line = word
        else:
            curr_line += " " + word

    final_text += curr_line
    return final_text

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("usage: ./meme.py <meme-name> <text-1> <text-2> ... <file_name>")
        print("where <meme-name> is one of")
        print([*memes_by_id.keys()])
    else:
        create_meme(sys.argv[1], sys.argv[2:-1], sys.argv[-1])
