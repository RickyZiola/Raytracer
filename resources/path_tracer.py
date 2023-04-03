from resources.vec3 import vec3
from resources.renderable import Renderable
import numpy as np

def trace(O, D, scene: list[Renderable], num_bounce = 3):
    c = vec3(np.ones_like(D.x))
    while num_bounce != 0:
        min_dist = np.full_like(D.x, np.inf)
        closest = np.empty_like(D.x, dtype=Renderable)
        for r in scene:
            d = r.intersect(O,D)
            closest = np.where(d < min_dist, r, closest)
            min_dist = np.where(d < min_dist, d, min_dist)
        for i,(dist,s) in enumerate(zip(min_dist,closest)):
            #print(c)
            #print(D)
            if(s == None):
                c[i] = vec3(0)
                continue
            #print(s.norm(O + D[i] * dist))
            c[i] = s.norm(O + D[i] * dist)
        return c
        num_bounce -= 1