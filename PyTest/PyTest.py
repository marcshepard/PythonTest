
"""My first Python module

Usage:
    python3 PyTest arg

    Prints the argument
"""

def print(arg):
    """Prints is arg and returns it.
    
    Args:
        arg: String argument to print.
    
    Returns:
        arg
    """
    print (arg)
    return arg


if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print ("Usage: test <string>")
    else:
        main(sys.argv[1])



