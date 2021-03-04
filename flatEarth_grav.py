import numpy as np
import time
 
def volume(r):
    return (4./3.) * (np.pi * r**3)

def grav_accel(p1, p2, m):
    """ p1 = point where the mass element is
        p2 = point you are interested in
        m  = mass
        returns a vector of the gravitational accleration"""
    G = 6.6743e-11
    r = np.sqrt(np.sum((p2 - p1)**2))
    rhat = (p2 - p1)/r
    return -1*G*m/r**2*rhat

def point_in_sphere(x,y,z, radius):
    if x**2 and y**2 and z**2 <= radius**2:    
        return True
    else:
        return False

if __name__ == "__main__":
    km = 1000 #1 km = 1000 meters
    rho = 5514 #kg/m^3, density of Earth
    r_earth = 20037*km #"radius" of flat Earth
    h = 628.3*km #relatively coarse step size scaled for increased "radius"
    dx, dy, dz = h, h, h #set grid size same in x,y,z
    #step size [h] and meshgrid scaled to match simulation for global Earth
    x = np.arange(-21991*km, 21991*km, dx)#x, y, z define boundaries of grid, here a hair over total "radius"
    len_x = x.shape[0]
    y = x.copy()
    z = np.arange(0,5000*km,dz)
    
    #defined points on the north pole, south pole, and equator
    #flat earth "Thickness" defines poles, and radius defines equator
    point_northpole = np.array([0, 0, 4750*km])
    point_equator   = np.array([10018.5*km,0,0])
    point_southpole = np.array([0,0,-4750*km])
    grav_vec_northpole = ([0,0,0])
    grav_vec_equator = ([0,0,0])
    grav_vec_southpole = ([0,0,0])
    
    for idx, xx in enumerate(x):
        #this is a trick to tell how long it will take
        print(idx, " of ", len_x, "x steps.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx,yy,zz,r_earth):
                    m = (rho * h**3) 
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
                    grav_vec_equator +=grav_accel(point,point_equator,m)
                    grav_vec_southpole += grav_accel(point,point_southpole,m)
    print("The gravity vector at the north pole is...", grav_vec_northpole)
    print("The gravity vector at the equator is...", grav_vec_equator)
    print("The gravity vector at the south pole is...", grav_vec_southpole)
    #shows the inconsistancy with gravity near poles compared to at equator