```
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count
```



This function works by iterating over all possible substrings of the given string. For each substring, it checks if the sum of the digits in the substring is equal to the length of the substring. If it is, it increments a counter. The function then returns the total count of such substrings. The unit test `assert count_Substrings('112112') == 6` ensures that the function is working correctly. 





# Python code for the problem
```
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count
```

# Explanation of the code

1. The function `count_Substrings(s)` takes a string `s` as input.
2. The variable `count` is initialized to 0, which will store the count of substrings with the sum of digits equal to their length.
3. The outer loop `for i in range(len(s)):` iterates over the indices of the string.
4. The inner loop `for j in range(i + 1, len(s) + 1):` generates all possible substrings of the string by iterating over the indices from `i` to the end of the string.
5. The substring `substring = s[i:j]` is generated using the indices `i` and `j`.
6. The condition `if sum(int(digit) for digit in substring) == len(substring):` checks if the sum of the digits in the substring is equal to the length of the substring.
7. If the condition is true, the count is incremented by 1 using `count += 1`.
8. The function returns the total count of substrings with the sum of digits equal to their length.

# Time complexity

The time complexity of this function is O(n^2), where n is the length of the input string. This is because the function generates all possible substr