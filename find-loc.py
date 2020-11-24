#!/usr/bin/env python3
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimage
import json
import time

def main():
    _, _, filenames = next(os.walk("./images"))

    with open("memes.json") as f:
        memes = json.load(f)

    for i, filename in enumerate(filenames):
        print(f"{len(filenames) - i - 1} memes not tagged")
        if filename in memes:
            continue

        default_identifier = filename.split(".")[0]
        identifier = input(f"Enter identifier for meme [default:{default_identifier}]:")
        identifier = default_identifier if identifier == "" else identifier
        text_points = []

        while True:
            f, a = plt.subplots()

            def onclick(e):
                text_points.append([e.xdata, e.ydata])
                plt.close()
            
            print("Keypress a meme text location:")
            img = mpimage.imread(f"./images/{filename}")
            imgplot = plt.imshow(img)
            f.canvas.mpl_connect("button_press_event", onclick)
            plt.show()

            while True:
                another_point = input("Add another text point [y/n]:").lower()
                if another_point in ["y", "n"]:
                    break
                print("please choose an option from y or n")

            if another_point == "n":
                break

        memes[filename] = {
                "identifier":identifier,
                "text_points": text_points,
        }

        with open("memes.json", "w") as f:
            json.dump(memes, f, indent=2)

if __name__ == "__main__":
    main()
