from resources.renderable import Renderable
from resources.vec3 import vec3
from resources.material import Material
import numpy as np

class Sphere(Renderable):
    c: vec3
    r: float
    mat: Material
    def __init__(self, center: vec3, radius: float, mat: Material):
        self.c = center
        self.r = radius
        self.mat = mat
    def intersect(self, O, D):
        b = 2 * D.dot(O - self.c)
        c = self.c.dot(self.c) + O.dot(O) - 2 * self.c.dot(O) - (self.r * self.r)
        disc = (b**2) - (4 * c)
        sq = np.sqrt(np.maximum(0, disc))
        h0 = (-b - sq) / 2
        h1 = (-b + sq) / 2
        h = np.where((h0 > 0) & (h0 < h1), h0, h1)
        pred = (disc > 0) & (h > 0)
        return np.where(pred, h, np.inf)
    
    def norm(self, pos):
        return (pos - self.c).norm()