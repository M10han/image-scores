import os
from PIL import Image
from PIL import ImageSequence
import numpy as np


def read_image(filename: str) -> np.ndarray:
    """Reads image from filename.

    Arguments:
        filename {str} -- Path to the file.

    Raises:
        RuntimeError: Unsupported file type error. Supported file types are {png, jpg, gif, bmp}

    Returns:
        np.ndarray -- Returns image as numpy array.
    """
    supported_file_extensions = ['.bmp', '.jpg', '.jpeg', '.gif', '.png']
    _, file_extension = os.path.splitext(filename)

    if file_extension.lower() not in supported_file_extensions:
        raise RuntimeError('Unsupported File format {}. Supported file formats are {}'.format(
            file_extension, supported_file_extensions))

    img = Image.open(filename)

    if file_extension.lower() == '.gif':
        frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
        img = frames[0].convert("RGB").copy()

    return np.asarray(img)
