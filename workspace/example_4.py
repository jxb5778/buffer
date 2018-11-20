from buffer import Buffer
import pandas as pd

"""
The reader Buffer will be used to hold a DataFrame that was just read in from a csv.
Each iteration of the loop will overwrite the value in reader.value -> forgetful worker pattern

Pandas concat is slow at scale, so we want to reduce the number of concats
Instead we append query results to a list, and then perform one pd.concat at the end
"""

# Not a real file list
DIRECTORY = 'C:/'
file_list = ['{0}example_file_{1}.csv'.format(DIRECTORY, index) for index in range(10)]

reader = Buffer()
query_return = Buffer()
query_return.value = []


# Look through all the files and find the results where Column == 12345
search_value = 12345

for file in file_list:
    reader.value = pd.read_csv(file)
    reader.value = reader.value.query('Column == @search_value')
    query_return.value.append(reader.value)

query_return.value = pd.concat(query_return.value)
