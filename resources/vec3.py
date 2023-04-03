import numpy as np

class vec3:
    x = np.array([], dtype=float)
    y = np.array([], dtype=float)
    z = np.array([], dtype=float)
    def __init__(self, x: 'np.array', y: 'np.array'=None, z: 'np.array'=None):
        
        if isinstance(y, type(None)):
            if isinstance(x, vec3):
                self.x = x.x.copy()
                self.y = x.y.copy()
                self.z = x.z.copy()
            else:
                self.x = x.copy()
                self.y = x.copy()
                self.z = x.copy()
        elif isinstance(z, type(None)):
            self.x = x
            self.y = y
            self.z = np.zeros_like(x,dtype=float)
        else:
            self.x = x
            self.y = y
            self.z = z
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    def length(self):
        return np.sqrt(self.dot(self))
    def norm(self):
        l = self.length()
        l = np.where(l == 0, 1, l)
        return self / l
    
    def components(self):
        return (self.x, self.y, self.z)
    def __getitem__(self,idx):
        return vec3(self.x[idx], self.y[idx], self.z[idx])

    def __setitem__(self, idx, item:'vec3'):
        self.x[idx] = item.x
        self.y[idx] = item.y
        self.z[idx] = item.z
    def set(self, idx, item: 'vec3'):
        self.x[idx] = item.x
        self.y[idx] = item.y
        self.z[idx] = item.z

    def __str__(self):
        return f'vec3({self.x}, {self.y}, {self.z})'
    

    def __abs__(self):
        return vec3(abs(self.x), abs(self.y), abs(self.z))
    def __add__ (self, other):
        if isinstance(other, vec3):
            return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        return vec3(self.x + other, self.y + other, self.z + other)
    def __radd__ (self, other):
        return self + other
    def __sub__ (self, other):
        if isinstance(other, vec3):
            return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        return vec3(self.x - other, self.y - other, self.z - other)
    def __mul__ (self, other):
        if isinstance(other, vec3):
            return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        return vec3(self.x * other, self.y * other, self.z * other)
    def __rmul__ (self, other):
        return self * other
    def __truediv__ (self, other):
        if isinstance(other, vec3):
            return vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        return vec3(self.x / other, self.y / other, self.z / other)
    
    def lerp(vec1, vec2, t):
        return vec3(vec1.x + (vec2.x - vec1.x) * t, vec1.y + (vec2.y - vec1.y) * t, vec1.z + (vec2.z - vec1.z) * t)

    