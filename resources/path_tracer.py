from resources.vec3 import vec3
from resources.renderable import Renderable
import numpy as np
import random

def trace(O, D, scene: list[Renderable], num_bounce = 2):
    c = vec3(np.ones_like(D.x, dtype=float))
    l = vec3(np.zeros_like(D.x, dtype=float))
    O *= D / D # reshape O
    O = vec3(O)
    D = vec3(D)
    return trace_internal(O, D, scene, c, l, num_bounce)
def trace_internal(O, D, scene: list[Renderable], c, l, num_bounce = 2):
    rand = np.random.default_rng(random.randint(0, 1000000))
    if num_bounce != -1:
        min_dist = np.full_like(D.x, np.inf)
        closest = np.full_like(D.x, None, dtype=Renderable)
        for r in scene:
            d = r.intersect(O,D)
            closest = np.where(d < min_dist, r, closest)
            min_dist = np.where(d < min_dist, d, min_dist)
        hit_pos = O + D * min_dist
        for i,s in enumerate(closest):
            if(s == None):
                c[i] *= vec3(0,0,0) # TODO: skybox
                continue
            hit = hit_pos[i]
            norm = s.norm(hit)
            