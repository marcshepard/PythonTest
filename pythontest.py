"""My first Python module

Usage:
    pythontest arg

Prints the argument
"""

import sys

def pyprint(arg):
    """Prints is arg and returns it.

    Args:
        arg: String argument to print.

    Returns:
        arg
    """
    print(arg)
    return arg


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise TypeError("Usage: pythontest <string>")
    else:
        pyprint(sys.argv[1])
