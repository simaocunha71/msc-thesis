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
The function `count_Substrings` takes a string `s` as input and returns the count of substrings with the sum of digits equal to their length. The function iterates over all possible substrings of the input string, calculates the sum of the digits in each substring, and checks if the sum is equal to the length of the substring. If it is, it increments the count. The function finally returns the count. The unit test `assert count_Substrings('112112') == 6` ensures the correctness of the function. 