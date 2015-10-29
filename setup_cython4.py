from distutils.core import setup, Extension
from Cython.Distutils import build_ext
setup(cmdclass={'build_ext': build_ext},
      ext_modules=[Extension("approx_pi_cython4",
                   sources=["approx_pi_cython4.pyx", "approx_pi.c"])])
