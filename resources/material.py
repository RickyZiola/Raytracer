from resources.vec3 import vec3
import numpy as np

class SubMaterial:
    color: vec3
    emission: vec3
    diffuse: float
    def __init__(self, color: vec3, emission: vec3, diffuse: float = 1.):
        self.color = color
        self.emission = emission
        self.diffuse = diffuse
class Material:
    diffuse: SubMaterial
    specular: SubMaterial
    specular_probability: float

    def __init__(self, diffuse: SubMaterial, specular: SubMaterial, specular_probability: float):
        self.diffuse = diffuse
        self.specular = specular
        self.specular_probability = specular_probability
