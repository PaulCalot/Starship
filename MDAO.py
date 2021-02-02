from scipy.integrate import solve_ivp
import math
# solve speed evolution

rho_air = 1.2 # kg/m3
g = 9.81 # m/s2
pi = math.pi

# fixed params 
mass_computer = 0.1 # 100 g - not the heaviest anyway
mass_battery = 0.3 # 300 g for a starter 

# --------------- Gaz speed after the propeller ------------- #

def u(v, X):
    m, Se, S, R, omega = X
    return 2*R*omega-v

# ---------------- Speed of the Starship --------------- #

# derivative of the speed w.r.t to time
def v_der(v, X): # dv/dt = v'
    m, Se, S, R, omega = X
    u = u(v, X)
    return(rho_air/m*(S*u*u-Se*v*v)-g)

# ---------- mass --------------- #

def volume(H, h, R, dR):
    return 2*pi*R*dR*(H+h/3.0)

def mass_structure(H, h, R, dR, rho):
    return volume(H, h, R, dR)*rho

def mass(mass_structure, mass_battery, mass_computer, mass_propeller):
    return mass_structure+mass_battery+mass_computer+mass_propeller

def mass_propeller(N, rho, r, L, e, R, w):
    # N number of blade
    # cylinder 
    mass_cylinder = pi*r*r*L*rho
    mass_blades = N*e*R*w # one blade is for now a cubic of size R*w*e - e : , R: radius, l : width, e : thickness
    return mass_cylinder+mass_blades
    


