"""Setup for this module"""
from distutils.core import setup

# To test setup, use a virtual python environment. From cmd:
#   > python3 -m venv pythontest_env
#   > pythontest_env/bin\activate
#   (pythontest_env) > python setup.py install  # Install directory will show ("copying")
#   (pythontest_env) > cd ..                    # Avoid conflict with source code dir
#   (pythontest_env) > python                   # Start python i firtual env
#   >>> import pythontest                       # Import module
#   >>> pythontest.__file__                     # Verify right import dir (see 4 lines above)
#   >>> ^q                                      # If all is well, then exit
#   > cd pythontest                             # Move back to source directory
#   > python setup.py sdist --format zip        # Package things up for redistribution
# Others can then use "pip install pythontest-1.0.zip" to install this module

setup(
    name='pythontest',
    version='1.0',
    py_modules=['pythontest'],

    #metadata
    author="Marc Shepard",
    author_email="myemail@mydomain.com",
    description="My first python module",
    license="None",
    keywords='test'
)
