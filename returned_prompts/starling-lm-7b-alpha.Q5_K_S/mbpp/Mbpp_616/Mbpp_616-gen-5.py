def tuple_modulo(tup1,tup2):
    result = []
    for i in range(len(tup1)):
        result.append(tup1[i]%tup2[i])
    return tuple(result)

# Driver program
print(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)))




"""
The above function creates an empty list called result. It then iterates through the tuples and takes the modulo of each pair of elements. It appends the modulo result to the result list. Finally, it returns the tuple created from the result list.
"""

"""
This function will return a tuple with the result of each element's modulo from the two input tuples.
"""

"""
The function works as follows:
1. It creates an empty list called result.
2. It iterates through the tuples using a for loop and the range function. The range function is used to get the indices of the tuples.
3. Inside the loop, it takes the modulo of the corresponding elements from tup1 and tup2 using the modulo operator (%). It then appends the result to the result list.
4. After the loop, it returns a tuple created from the result list using the tuple function.
"""

"""
This function can be used to perform element wise modulo on two tuples of the same length. It returns a tuple with the results of each element's modulo operation.
"""

"""
For example, if we call the function with the tuples (10, 4, 5, 6) and (5, 6, 7, 5), it will return the tuple (0, 4, 5, 1). This is because the modulo of 10 and 5 is 0, the modulo of 4 and 6 is 4, the modulo of 5 and 7 is 5, and the modulo of 6 and 5 is 1.
"""

"""
The function can be tested by using the assert statement to check if the result of the function is equal to the expected result. In this case, the expected result is the tuple (0, 4, 5