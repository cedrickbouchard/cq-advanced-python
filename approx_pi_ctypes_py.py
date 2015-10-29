# approx_pi_ctypes.py
""" Example of wrapping approx_pi using ctypes. """

import ctypes

# find and load the library
approx_pi_dll = ctypes.cdll.LoadLibrary('./approx_pi_ctypes.so')
# set the argument type
approx_pi_dll.approx_pi.argtypes = [ctypes.c_int]
# set the return type
approx_pi_dll.approx_pi.restype = ctypes.c_double

def approx_pi(arg):
    ''' Wrapper for approx_pi '''
    return approx_pi_dll.approx_pi(arg)

