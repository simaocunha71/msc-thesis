```
def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]
```
The function `index_minimum` takes a list of tuples as input and returns the first value of the tuple with the smallest second value. The `min` function is used with a lambda function as the key to specify that the second value of each tuple should be compared. The `[0]` indexing is used to extract the first value of the tuple returned by the `min` function. For example, the function `index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)])` returns 'Varsha', which is the first value of the tuple with the smallest second value (100).  """

The unit test `assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'` helps to clarify the expected behavior of the function. It shows that the function should return the first value of the tuple with the smallest second value. This is achieved by using the `min` function with a lambda function as the key, which compares the second value of each tuple. The `[0]` indexing is used to extract the first value of the tuple returned by the `min` function.  """

The function is designed to work with a list of tuples, where each tuple contains a value and a corresponding index. The function returns the value with the smallest index. The unit test helps to ensure that the function behaves as expected.  """

The time complexity of the function is O(n), where n is the number of tuples in the input list. This is because the `min` function iterates over the input list once to find the tuple with the smallest second value. The space complexity is O(1), which means the function uses a constant amount of space to store the result, regardless of the size of the input list.  """

The function is a simple and efficient solution to the problem. It uses the built-in `min` function with a lambda function as the key to find the tuple with the smallest second value, and then returns the first value of that tuple.  """

The function is easy to understand and maintain. It is a single line of code, and it is easy to see what the function does by reading the code. The use of the `min` function and the lambda function makes the code concise and easy to read.  """

The function is a good