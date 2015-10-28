#cython:cdivision=True
import math
import time

def approx_pi(int intervals):
    cdef double pi
    cdef int i
    pi = 0.0
    for i in range(intervals):
        pi += (4 - 8 * (i % 2)) / (float)(2 * i + 1)
    return pi

t1 = time.clock()
pi = approx_pi(100000000)
t2 = time.clock()
print("PI is approximately %.16f, Error is %.16f"%(pi, abs(pi - math.pi)))
print("Time = %.16f sec\n"%(t2 - t1))
