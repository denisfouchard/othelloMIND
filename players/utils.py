import numpy as np

def build_wmap() -> np.ndarray:
    wmap = np.ones((8, 8))

    # Add weights to the four edges
    wmap[0, :] += 1
    wmap[7, :] += 1
    wmap[:, 0] += 1
    wmap[:, 7] += 1

    # Add weights to the four corners
    wmap[0, 0] += 3
    wmap[0, 7] += 3
    wmap[7, 0] += 3
    wmap[7, 7] += 3

    return wmap