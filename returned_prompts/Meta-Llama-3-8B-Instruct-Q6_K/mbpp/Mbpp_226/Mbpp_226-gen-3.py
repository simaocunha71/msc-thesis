```
def odd_values_string(s):
    return ''.join([c for i, c in enumerate(s) if i % 2 == 0])
```
Explanation:
The problem is asking to remove the characters which have odd index values of a given string. We can achieve this by using list comprehension and the `enumerate` function to get both the index and value of each character in the string. We then filter the characters to only include those with even index values and join them back into a string. The `assert` statement provided in the problem ensures the function works correctly for the given example. 





This function takes a string `s` as input and returns a new string with only the characters at even index positions. The `enumerate` function is used to iterate over the string and get both the index and value of each character. The list comprehension then filters the characters to only include those with even index values, and the `join` method is used to concatenate these characters back into a string. This new string is then returned by the function.