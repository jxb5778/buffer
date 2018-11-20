from buffer import Buffer

# We'll start of by learning how to set the value property of a Buffer


def main():
    pass

if __name__ == '__main__':
    import __main__

    buff = Buffer()
    buff.value = 5
    print(buff.value)

    print(__main__.__dict__)

    """
    Creating a Buffer identifies a specific location in memory we can store its value attribute
    We can use this to our advantage when we store DataFrames in value -> explored further in Example 3
    
    Output ->
    
    {
    '__name__': '__main__', 
    '__doc__': None, 
    '__package__': None, 
    '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x038EDC90>, 
    '__spec__': None, 
    '__annotations__': {}, 
    '__builtins__': <module 'builtins' (built-in)>, 
    '__file__': 'C:/Users/bergj/PycharmProjects/buffer/workspace/example_2.py', 
    '__cached__': None, 
    'Buffer': <class 'buffer.Buffer'>, 
    'main': <function main at 0x03B6B030>, 
    '__main__': <module '__main__' from 'C:/Users/bergj/PycharmProjects/buffer/workspace/example_2.py'>, 
    'buff': <buffer.Buffer object at 0x038EDD10>
    }
    
    """
