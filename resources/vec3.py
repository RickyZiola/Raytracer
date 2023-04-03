import numpy as np

class vec3:
    def __init__(self, x: 'np.array', y: 'np.array'=None, z: 'np.array'=None):
        
        if y is None:
            if isinstance(x, vec3):
                self.x = x.x
                self.y = x.y
                self.z = x.z
            else:
                self.x = x
                self.y = x
                self.z = x
        elif z is None:
            self.x = x
            self.y = y
            self.z = 0
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
    def __setitem__(self, idx, item):
        self.x[idx] = item.x
        self.y[idx] = item.y
        self.x[idx] = item.z
    def __str__(self):
        return f'vec3({self.x}, {self.y}, {self.z})'
    
    def __add__ (self, other):
        if isinstance(other, vec3):
            return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        return vec3(self.x + other, self.y + other, self.z + other)
    def __sub__ (self, other):
        if isinstance(other, vec3):
            return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        return vec3(self.x - other, self.y - other, self.z - other)
    def __mul__ (self, other):
        if isinstance(other, vec3):
            return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        return vec3(self.x * other, self.y * other, self.z * other)
    def __truediv__ (self, other):
        if isinstance(other, vec3):
            return vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        return vec3(self.x / other, self.y / other, self.z / other)

    