import numpy as np
from PIL import Image

import math
import time

import sys

w = 426
h = 240
r = float(w) / h

if __name__ == "__main__":
    # TODO: implement raytracer
    from resources.vec3 import vec3
    from resources.sphere import Sphere
    from resources.path_tracer import trace

    E = vec3(0, .5, -1)
    scene = [
        Sphere(vec3(0, 0, 1), .6)
    ]
    S = (-1, 1 / r + .25, 1, -1 / r + .25)
    x = np.tile(np.linspace(S[0], S[2], w), h)
    y = np.repeat(np.linspace(S[1], S[3], h), w)

    t0 = time.time()
    Q = vec3(x, y, 0)
    D=(Q - E).norm()
    color = trace(E, D, scene)
    lrgb = [
        Image.fromarray((255 * np.clip(c, 0, 1).reshape(
            (h, w))).astype(np.uint8))
            for c in color.components()
        ]
    Image.merge("RGB", lrgb).save("rt3.png")