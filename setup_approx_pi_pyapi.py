from distutils.core import setup, Extension
# define the extension module
module = Extension('approx_pi_pyapi', sources=['approx_pi_pyapi.c', 'approx_pi.c'])
# run the setup
setup(ext_modules=[module])
