import numpy as np
import time

def function_to_integrate(x):
    """Function to be tested"""
    return 4*((b / a)*np.sqrt(a**2 - x**2))
    
def ellipse_area(a,b):
    """Calculates ellipse area traditionally using semi-major and semi-minor axis values"""
    return(np.pi*a*b)

def trapezoidal_rule(f, a=None, b=None, n=None):
    """
    Given a function to integrate, a starting point, ending point, and number of points between
    this function will calculate the integral using the trapezoidal rule (trapezoid fitted segments to curve)
    Input: function, a(start), b(end), n(number of points)
    Output: Integral of given function (quite accurate)
    """
    h = (b - a)/n
    value = 0.
    for x in np.linspace(a, b - h, n - 1): #a, b-h to avoid going too far (minus 1 step.) n - 1 to avoid extra count
        value += 0.5 * (f(x + h)+f(x))  
    return value*h
    
if __name__ == "__main__":
    a = 2. #semi-minor axis
    b = 4. #semi-major axis
    n = 1000 #number of steps for closer integral approx (increase to reduce error)
    origin = 0. #center of ellipse
    ellipse_int = trapezoidal_rule(function_to_integrate,origin,a,n) #integrate from origin to semi-minor axis (4 quarters of ellipse area)
    true = ellipse_area(a,b)
    print('\n')
    print('The calculated area using trapezoidal rule is:',ellipse_int)
    print('The true area of the ellipse is:',true)
    print('\n')
    t = time.time()
    h = 0.001
    x = np.arange(-4,4,h)
    y = np.arange(-4,4,h)
    xs,ys = np.meshgrid(x,y)
    mask = 2.0*(xs**2 + ys**2 <=4)
    dx = h
    dy = h
    total_value = np.sum(mask*dx*dy)
    
    print('Using 2D analysis, the area is:',total_value)
    t1 = time.time()
    time_total = t1 - t
    print('Time to compute 2D analysis:',time_total)