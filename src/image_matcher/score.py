import typing
import numpy as np
from skimage.metrics import structural_similarity as ssim


def bjorn_score(image1: np.ndarray, image2: np.ndarray) -> float:
    """Calculates the Bjorn score of two input images.
    0    = Two images are perfectly similar
    <0.1 = Two images are structurally similar
    1    = Two images are not similar

    Arguments:
        image1 {np.ndarray} -- Image 1
        image2 {np.ndarray} -- Image 2

    Returns:
        float -- bjorn score of image1 and image2
    """
    if image1.shape != image2.shape:
        # Images not matching
        return 1.0

    score = 1.0 - ssim(image1, image2, multichannel=True)
    return score
