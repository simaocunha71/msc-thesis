```python
def number_of_substrings(string):
    length = len(string)
    substrings = 0
    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings += 1
    return substrings

def test_number_of_substrings():
    assert number_of_substrings("abc") == 6
    print("All Test cases passed.")

test_number_of_substrings()
```

Explanation:
This function counts the number of non-empty substrings in a given string. It uses two nested loops to iterate through all possible substrings of the string. The outer loop starts at the first character and the inner loop starts at the next character. For each combination of start and end indices, the function increments the count. Finally, it returns the total count of substrings.
The test function `test_number_of_substrings` asserts that the function correctly counts the number of substrings in the example string "abc". It then prints a message indicating that all test cases have passed.

To use this function, you can simply call `number_of_substrings` with a string as the argument. It will return the number of non-empty substrings in that string.

In the given example, `number_of_substrings("abc")` returns 6, as there are six non-empty substrings in the string "abc": "a", "ab", "abc", "b", "bc", and "c".

This solution is a simple and efficient way to count the number of non-empty substrings in a given string using Python.

You can also use this function to count the number of non-empty substrings in any