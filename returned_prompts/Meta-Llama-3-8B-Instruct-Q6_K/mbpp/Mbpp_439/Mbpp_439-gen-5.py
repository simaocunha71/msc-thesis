The problem asks to write a function that takes a list of integers as input and returns a single integer. The single integer is formed by concatenating the digits of the input integers in the order they appear.

For example, if the input is [11, 33, 50], the function should return 113350. This is because the digits of the input integers are concatenated in the order they appear: 11 becomes 11, 33 becomes 33, and 50 becomes 50, resulting in the final output 113350.

Here is a Python solution for the problem:
```
def multiple_to_single(lst):
    result = ''
    for num in lst:
        result += str(num)
    return int(result)
```
This function iterates over each integer in the input list, converts each integer to a string, and appends it to the result string. Finally, it converts the result string to an integer and returns it. The unit test `assert multiple_to_single([11, 33, 50])==113350` ensures that the function works correctly.