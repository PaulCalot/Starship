from scipy.integrate import RK45
from numpy import numpy

class RK45():
    def __init__(self, fun, t0, y0, t_bound, max_step= np.inf,\
                 rtol=0.001, atol=1e-6):
        self.scheme = RK45(fun, t0, y0, t_bound, \
                           max_step = max_step, \
                           rtol = rtol, atol = atol)
        self.t = [t0]
        self.y = [y0]
    
    def step(self):
        self.scheme.step()
        self.t.append(self.scheme.t)
        self.y.append(self.scheme.y)
    
    def simulate(self):
        
    