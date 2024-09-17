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
This function iterates over all possible substrings of the input string `s` and checks if the sum of the digits in the substring is equal to the length of the substring. If it is, it increments the count. The function finally returns the total count of such substrings. The unit test `assert count_Substrings('112112') == 6` ensures that the function is working correctly.