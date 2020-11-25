#!/usr/bin/env python3
import yaml
import subprocess
from meme import create_meme


with open("./memes.yaml") as f:
    memes = yaml.safe_load(f)

    for i, (filename, meme) in enumerate(memes.items()):
        print(f"completed {i+1} of {len(memes)} memes to render")
        texts = [f"text {i}" for i in range(len(meme['text_points']))]
        create_meme(meme["identifier"], texts, f"./samples/sample-{filename}")
        texts = [f"text some super long text over here lol just text text text texty texty texty mmm something something something {i}" for i in range(len(meme['text_points']))]
        create_meme(meme["identifier"], texts, f"./samples/sample-longtext-{filename}")

with open("./meme-samples.md", "w") as f:
    f.write("# meme samples\n")
    f.write("samples for the provided memeing options\n")
    f.write("\n\n\n")
    for i, (filename, meme) in enumerate(memes.items()):
        f.write(f"## {i}, {meme['identifier']}\n\n")
        f.write(f"![{meme['identifier']} sample](./samples/sample-{filename})\n")
        f.write(f"![{meme['identifier']} sample](./samples/sample-longtext-{filename})\n\n\n\n")

subprocess.run("python3 -m markdown meme-samples.md > meme-samples.html", shell=True)
