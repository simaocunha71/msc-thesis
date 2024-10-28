```
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count
```


In this problem, we need to write a function that counts the number of substrings in a given string where the sum of the digits in the substring is equal to the length of the substring.

The unit test `assert count_Substrings('112112') == 6` suggests that the function should count all substrings in the given string, not just the ones that appear in the same order as the input string.

Here is a Python function that solves the problem:

```
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count
```

This function uses two nested loops to generate all substrings of the input string. It then checks each substring to see if the sum of its digits is equal to its length. If it is, the function increments a count. Finally, the function returns the count.

The function works by iterating over each character in the input string, and then iterating over each possible end point for a substring. It then generates the substring by slicing the input string from the start index to the end index, and checks if the sum of its digits is equal to its length. If it is, the function increments a count. Finally, the function returns the count.