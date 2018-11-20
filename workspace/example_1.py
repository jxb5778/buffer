
# Everything in Python is an object
# Here we'll explore attributes of main()


def main():
    num = 5
    return num


if __name__ == '__main__':
    import __main__

    num = main()

    print(__main__.__dict__)

    """ 
    Output -> notice the variable num we created is in main's __dict__ attribute
    
    {
    '__name__': '__main__', 
    '__doc__': None, 
    '__package__': None, 
    '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x009DDC90>, 
    '__spec__': None, 
    '__annotations__': {}, 
    '__builtins__': <module 'builtins' (built-in)>, 
    '__file__': 'C:/Users/bergj/PycharmProjects/buffer/workspace/example_1.py', 
    '__cached__': None, 
    'main': <function main at 0x0104B030>, 
    '__main__': <module '__main__' from 'C:/Users/bergj/PycharmProjects/buffer/workspace/example_1.py'>, 
    'num': 5
    }
    
    """
