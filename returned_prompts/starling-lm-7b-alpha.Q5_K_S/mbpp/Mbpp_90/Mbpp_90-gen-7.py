"""
def len_log(arr):
    max = 0
    for i in range(len(arr)):
        if(len(arr[i])>max):
            max = len(arr[i])
    return max

"""
This function will return the length of the longest word in the list. It takes a list of strings as an argument and iterates over each string in the list to find the maximum length.

Here is a step-by-step explanation of the function:

1. Initialize a variable `max` to 0, which will store the length of the longest word.
2. Iterate over each string in the list using a `for` loop and the `range(len(arr))` expression. This will give us the index of each string in the list.
3. Inside the loop, use the `len()` function to find the length of the current string and compare it with the value of `max`. If the length of the current string is greater than the value of `max`, update `max` to the length of the current string.
4. After iterating over all the strings in the list, return the value of `max`, which will be the length of the longest word in the list.
5. To test the function, use the `assert` statement to check if the function returns the correct result for the given input `["python","PHP","bigdata"]`. The expected output is 7, which is the length of the word "bigdata".

The function can be used in the following way:

```python
print(len_log(["python","PHP","bigdata"]))  # Output: 7
```

This will print the length of the longest word in the list `["python","PHP","bigdata"]`, which is 7.

"""

# Python3 Program to find the length of the longest word
def len_log(arr):
    max = 0
    for i in range(len(arr)):
        if(len(arr[i])>max):
            max = len(arr[i])
    return max

# Driver program
print(len_log(["python","PHP","bigdata"]))  # Output: 7

# This code is contributed by 
# Shubham Singh(SHUBHAM