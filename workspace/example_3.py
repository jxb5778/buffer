from buffer import Buffer
import pandas as pd

# Here we're expanding the scope of two Buffer variables, and exploring DataFrame transformations
# Best practice -> pass Buffers to functions, don't pass and return DataFrames


def func_1(buff_1, buff_2):
    buff_1.value = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 2, 3, 4, 5]})
    buff_2.value = pd.DataFrame({'A': [5, 4, 3, 2, 1], 'B': [50, 40, 30, 20, 10]})
    return


def func_2(buff_1, buff_2):
    buff_1.value = [buff_1.value, buff_2.value]
    buff_1.value = pd.concat(buff_1.value)
    buff_1.value['C'] = buff_1.value['A'] + buff_1.value['B']
    buff_2.value = None
    return


buff_a = Buffer()
buff_b = Buffer()

func_1(buff_a, buff_b)
print('Buffer a value:\n{0}\nBuffer b value:\n{1}'.format(buff_a.value, buff_b.value))

func_2(buff_a, buff_b)
print('Buffer a value:\n{0}\nBuffer b value:\n{1}'.format(buff_a.value, buff_b.value))
