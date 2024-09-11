"""
To solve this problem, you can follow these steps:

1. Define a function called index_minimum that takes a list of tuples as an argument.
2. Inside the function, initialize a variable called minimum_index with the index of the first tuple in the list (i.e., 0).
3. Initialize a variable called minimum_value with the second value of the first tuple (i.e., 143).
4. Use a for loop to iterate over the range of the length of the list. For each index, do the following:
   a. Get the second value of the tuple at that index.
   b. Compare the second value with the current minimum_value. If it is smaller, update minimum_value and minimum_index with the new values.
5. After the loop, return the first value of the tuple at minimum_index.
6. Define a test function called test_index_minimum that checks if the index_minimum function is working correctly. It should call the index_minimum function with the provided example list of tuples and assert that the returned value is 'Varsha'.
7. Finally, call the test_index_minimum function to verify the correctness of the index_minimum function.
"""

def index_minimum(list_of_tuples):
    minimum_index = 0
    minimum_value = list_of_tuples[0][1]
    for index in range(len(list_of_tuples)):
        if list_of_tuples[index][1] < minimum_value:
            minimum_value = list_of_tuples[index][1]
            minimum_index = index
    return list_of_tuples[minimum_index][0]

def test_index_minimum():
    assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'

test_index_minimum()

# This code defines a function called index_minimum that takes a list of tuples as an argument and returns the first value of the tuple with the smallest second value. The function initializes a variable called minimum_index with the index of the first tuple in the list, and