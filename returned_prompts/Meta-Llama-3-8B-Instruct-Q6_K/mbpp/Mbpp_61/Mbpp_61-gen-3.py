```
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count
```



This function iterates over all possible substrings of the input string `s`. For each substring, it checks if the sum of its digits is equal to its length. If it is, it increments the `count` variable. Finally, it returns the total count of substrings with the desired property.

The unit test `assert count_Substrings('112112') == 6` ensures that the function works correctly. It checks that the function returns 6 for the input string '112112', which has 6 substrings with the sum of digits equal to their length.

Note that this function has a time complexity of O(n^2), where n is the length of the input string, because it uses two nested loops to generate all possible substrings. This may not be efficient for very large input strings. If efficiency is a concern, a more efficient algorithm could be used. However, for most practical purposes, this function should work correctly and efficiently.