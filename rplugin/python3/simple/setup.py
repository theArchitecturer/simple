from setuptools import setup
from Cython.Build import cythonize

setup(
    name = "simple plugins",
    ext_modules = cythonize("__init__.pyx"),
    zip_safe = False
)
