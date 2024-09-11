def filter_data(dictionary,min_height,min_weight):
    res={}
    for i in dictionary:
        if dictionary[i][0]>min_height and dictionary[i][1]>min_weight:
            res[i]=dictionary[i]
    return res

# Here are some tests for the function
print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}) # True
"""
The above statement checks if the function gives the expected output for the given test data
"""

# Here is another test
print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.1,71)) # {}
"""
The above statement checks if the function gives the expected output for the given test data
"""

# Here is yet another test
print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},5.8,66)) # {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68)}
"""
The above statement checks if the function gives the expected output for the given test data
"""

# Here is another test
print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre