```
def number_of_substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            count += 1
    return count
```
This function works by iterating over the string and for each character, it generates all possible substrings (from the current character to the end of the string) and counts them. The time complexity of this function is O(n^2), where n is the length of the string. 

For example, for the input "abc", the function generates the following substrings: "a", "ab", "abc", "b", "bc", "c", and counts them. The total count is 6. 

Note: The unit test `assert number_of_substrings("abc") == 6` ensures that the function is working correctly. 

However, there is a more efficient way to solve this problem. We can use the formula `n*(n+1)/2` to calculate the number of non-empty substrings of a string, where `n` is the length of the string. This is because the number of non-empty substrings of a string of length `n` is equal to the sum of the first `n` positive integers, which is `n*(n+1)/2`. 

Here is the updated function:
```
def number_of_substrings(s):
    return len(s) * (len(s) + 1) // 2
```
This function has a time complexity of O(1), which is much more efficient than the previous function. 

For example, for the input "abc", the function returns `3 * (3 + 1) // 2 = 6`, which is the correct answer. 

This updated function is more efficient and easier to understand, and it passes the given unit test. 