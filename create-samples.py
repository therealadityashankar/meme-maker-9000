#!/usr/bin/env python3
import json
import subprocess
from meme import create_meme


with open("./memes.json") as f:
    memes = json.load(f)

    for filename, meme in memes.items():
        texts = [f"text {i}" for i in range(len(meme['text_points']))]
        create_meme(meme["identifier"], texts, f"./samples/sample-{filename}")

with open("./meme-samples.md", "w") as f:
    f.write("# meme samples\n")
    f.write("samples for the provided memeing options\n")
    f.write("\n\n\n")
    for filename, meme in memes.items():
        f.write(f"## {meme['identifier']}\n")
        f.write(f"![{meme['identifier']} sample](./samples/sample-{filename})\n\n")

subprocess.run("python3 -m markdown meme-samples.md > meme-samples.html", shell=True)
