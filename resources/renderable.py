from resources.vec3 import vec3
import numpy as np

class Renderable:
    def intersect(self, O, D):return np.full_like(D, np.inf)
    def norm(self, pos):return vec3(np.ones_like(pos.x))