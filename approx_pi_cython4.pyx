cdef extern from "approx_pi.h":
    double c_approx_pi "approx_pi" (int intervals)

def approx_pi(int intervals):
    return c_approx_pi(intervals)
