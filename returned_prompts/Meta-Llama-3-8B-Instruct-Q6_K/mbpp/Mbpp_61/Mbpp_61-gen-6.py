```
def count_Substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count
```


The problem is asking to write a function that counts the number of substrings in a given string where the sum of digits in the substring is equal to its length. For example, for the string '112112', the function should return 6 because there are 6 substrings with this property: '1', '1', '11', '11', '112', '112'.

The unit test `assert count_Substrings('112112') == 6` helps to understand the problem better. It implies that the function should count all substrings that meet the condition, not just the longest ones.

Here is the Python solution for the problem:
```
def count_Substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count
```
This function iterates over all possible substrings of the given string and checks if the sum of digits in the substring is equal to its length. If it is, it increments the count. Finally, it returns the count. The function works for any string, not just the one given in the unit test.