# cq-formation-advanced-python
Advanced and Parallel Python workshop material

Notes: 
pi_collect.py imports from the sys args via __import__

vectorized code (approx_pi_numpy) is slower because you need to create/operate on large arrays.

Python API: 
Lots of extra code,
Version dependent.
Compiled using a setup file (you can then import your C function in python)
Once imported, you can use help(), or any other operation that would work on a module.

Boilerplate code:
"Red tape", code with no other function than make the module work.

CTypes:Wrapper file is written in python rather than C.
The C file is compiled as a share object. You then import cTypes and load your library. you then have to specify the args and return types. You ten wrap the function (see approx_pi_ctypes_py.py)


Shared files: .so in linux, dll in windows, dylib on macos

SWIG:
Mature techonology, uses distutils like the CTypes, but generates automatically 3 filesusing python (rather than gcc). (see i-files)
Creates very large CFiles (100 kb for approx pi) making it large to debug.

Cython:
Compiles python .pyx files into automatically generated C files (see setup_cython) for details.
About a factor of 2 faster than native python, unless you annotate (explicit typing)
The more we explicit the Python script, the closer we get Cs performance (applies to types, operators and functions). 
(python's float is C's double)
Interfacing is done with cdef in the pyx file. Care for naming conflicts. 
We can then build (somewhat like with SWIG) (see setuP_cython4.py) 


Parallel Programming Concepts
Serial tasks: Communication, IO, startup/cleanup. 
//tasks:
Data parallelism:same action on multiple dataset
Process parallelism:multiple actions on a given dataset

Multiprocessing Module:
workers need a tuple (might have to hack code to make it works)
worker call is synchronous.

Callback function will be called once process is over
