
def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

"""
In the key parameter of the sorted() function, we define a lambda function that 
returns a tuple. The first element of the tuple is the count of ones in the binary 
representation of the number, and the second element is the number itself. 

This way, Python sorts the array first by the count of ones in the binary representation, 
and then by the decimal value of the number.
"""

