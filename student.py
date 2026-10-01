import math
import numpy as np


class Student:

    def __init__(self, i, n, d):
        self.id, self.name, self.dob = i, n, d
        self.marks, self.gpa = {}, 0.0

    def calc_gpa(self, C):
        m = [self.marks[c.id] for c in C if c.id in self.marks]
        w = [c.credit for c in C if c.id in self.marks]
        self.gpa = math.floor(np.average(m, weights=w) * 10) / 10 if w else 0.0