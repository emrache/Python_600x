# f(x), as referenced in radationExposure function
## x is a measure of time, f(x) returns y, the height of the curve
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    float=0
    ##base case if stop-start = step:
    if stop - start == step:
        float = f(start)*step
    ##base case if stop-start < step
    elif stop - start < step:
        float = f(start)*(stop-start)
    else:
        float = f(start)*step + radiationExposure (start+step, stop, step)
        print 'radiationExposure (' + str(start+step) +')'
    return float
