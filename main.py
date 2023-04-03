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
    from resources.material import Material, SubMaterial

    diffuseMaterial = SubMaterial(vec3(1, 0, 0), vec3(0,0,0))
    specularMaterial = SubMaterial(vec3(0, 1, 0), vec3(0,0,0))

    lightMaterial = SubMaterial(vec3(0, 0, 0), vec3(1,1,1))

    sphereMaterial = Material(diffuseMaterial, specularMaterial, 0)
    sphereMaterial2 = Material(lightMaterial, specularMaterial, 0)
    E = vec3(0, .5, -1)
    scene = [
        Sphere(vec3(-5, 5, 10), 2, sphereMaterial2),
        Sphere(vec3(-1, 0, 1), .6, sphereMaterial),
        Sphere(vec3(1, 0, 1), .6, sphereMaterial),
        Sphere(vec3(0, -9999.6, 1), 9999, sphereMaterial)
    ]
    S = (-1, 1 / r + .25, 1, -1 / r + .25)
    x = np.tile(np.linspace(S[0], S[2], w), h)
    y = np.repeat(np.linspace(S[1], S[3], h), w)

    t0 = time.time()
    Q = vec3(x, y, 0)
    D=(Q - E).norm()
    p_c = []
    while True:
        color = trace(E, D, scene)
        p_c.append(color)
        color = sum(p_c) / len(p_c) # progressive rendering
        print('frame')
        lrgb = [
            Image.fromarray((255 * np.clip(c, 0, 1).reshape(
                (h, w))).astype(np.uint8))
                for c in color.components()
            ]
        Image.merge("RGB", lrgb).save("rt3.png")