def empty_list(N):
    return [{} for _ in range(N)]


Explanation:
This problem asks to create a function that generates a list of N empty dictionaries. 

The unit test `assert empty_list(5)==[{},{},{},{},{}]` suggests that the function should take an integer N as input and return a list of N empty dictionaries.

The solution is a simple list comprehension that creates N empty dictionaries. It uses the `_` variable to ignore the loop variable since it's not used in the expression. The function then returns this list of dictionaries. 

For example, calling `empty_list(5)` would return `[{},{},{},{},{}]`. 