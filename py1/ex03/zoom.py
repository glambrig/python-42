from load_image import ft_load
from PIL import Image
import numpy as np


def printNewStats(img: Image) -> None:

    flag = False

    # if it needs to be grayscale (confusing subject), uncomment this
    flag = True
    img = img.convert("L")

    w = img.width
    h = img.height
    b = len(img.getbands())

    if flag is False:
        print(f"The shape of the image is: ({w} {h} {b})")
        print(np.array(list(img.getdata())))
    else:
        print(f"The shape of the image is: ({w} {h} {b}) or ({w}, {h})")
        print(np.array(list(img.getdata())))


def main():
    '''
    Create a program that should load the image "animal.jpeg",
    print some information
    about it and display it after "zooming".
    '''

    try:
        img = Image.open("animal.jpeg")
        imgInfo = ft_load("animal.jpeg")
        assert imgInfo is not None, "Image is empty"
    except AssertionError as err:
        print(f"AssertionError: {err}")
        return
    except Exception as err:
        print(f"Exception occurred: {err}")
        return

    print(imgInfo)

    left = img.width / 4
    right = img.width - left
    top = img.height / 4
    bottom = img.height - top
    img = img.crop((left, top, right, bottom))

    printNewStats(img)


if __name__ == "__main__":
    main()
