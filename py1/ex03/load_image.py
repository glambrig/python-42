from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    '''You need to write a function that loads an image,
    prints its format, and its pixels
    content in RGB format.
    You have to handle, at least, JPG and JPEG format'''

    try:
        img = Image.open(path)
        assert img is not None, "Image failed to load"
        assert img.format == "JPEG" or img.format == "JPG", "Type unsupported"
    except AssertionError as err:
        print(f"AssertionError: {err}")
        return
    except Exception as err:
        print(f"Exception occurred: {err}")
        return

    # print picture dimensions: (width height numberOfChannels)
    w = img.width
    h = img.height
    b = len(img.getbands())
    print(f"The shape of the image is: ({w}, {h}, {b})")

    return np.array(list(img.getdata()))
