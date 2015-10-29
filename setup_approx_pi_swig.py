from distutils.core import setup, Extension
# define the extension module
module = Extension('_approx_pi_swig', sources=['approx_pi.c', 'approx_pi_swig.i'])
# run the setup
setup(ext_modules=[module])
