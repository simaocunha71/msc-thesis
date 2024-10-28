def new_tuple(list, string):
    return tuple(list + [string])  # Convert list to tuple and add string to it

assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')  # Check if the function works correctly
print(new_tuple(["WEB", "is"], "best"))  # Output: ('WEB', 'is', 'best')  # Check the output
print(type(new_tuple(["WEB", "is"], "best")))  # Output: <class 'tuple'>  # Check the type of output
print(new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best'))  # Output: True  # Check if the output is as expected

Output:
('WEB', 'is', 'best')

Explanation:
The function new_tuple takes two parameters: a list and a string. It converts the list to a tuple and then adds the string to the tuple. This new tuple is then returned. The unit test provided ensures that the function works correctly by checking if the output is the expected tuple. The output is indeed the expected tuple and is of type tuple. The last part of the unit test checks if the output is equal to the expected tuple, which is also True. Therefore, the function is working correctly.