/*  Example of wrapping approx_pi() with the Python-C-API. */
#include <Python.h>
#include "approx_pi.h"
static PyObject* approx_pi_func(PyObject* self, PyObject* args)
{   /*  wrapped approx_pi function */
    int value; double answer;
    /*  parse the input, from python float to c double */
    if (!PyArg_ParseTuple(args, "i", &value))
        return NULL;
    /* if the above function returns -1, an appropriate Python exception will
     * have been set, and the function simply returns NULL */
    answer =approx_pi(value);
    /*  construct the output from approx_pi, from c double to python float */
    return Py_BuildValue("f", answer);
}

/*  define functions in module */
static PyMethodDef PiMethods[] =
{
    {"approx_pi", approx_pi_func, METH_VARARGS, "approximate Pi"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef PiModule = {
    PyModuleDef_HEAD_INIT,
    "approx_pi_pyapi", NULL, -1,
    PiMethods,
    NULL, NULL, NULL, NULL
};

/* module initialization */
PyMODINIT_FUNC
PyInit_approx_pi_pyapi(void)
{
    (void) PyModule_Create(&PiModule);
}



