import numpy

def approx_pi(intervals):
    pi1 = 4/numpy.arange(1, intervals*2, 4)
    pi2 = -4/numpy.arange(3, intervals*2, 4)
    return numpy.sum(pi1) + numpy.sum(pi2)
