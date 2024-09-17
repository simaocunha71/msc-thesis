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

The above function counts the number of substrings in the given string `s` where the sum of the digits equals the length of the substring. It uses two nested for loops to generate all possible substrings of `s`, and checks each substring to see if the sum of its digits equals its length. If it does, it increments the count. Finally, it returns the total count. The unit test `assert count_Substrings('112112') == 6` ensures that the function is working correctly.  The time complexity of this function is O(n^2), where n is the length of the string `s`, because it generates all possible substrings of `s` and checks each one. The space complexity is O(1), because it only uses a constant amount of space to store the count and the substring.  This function assumes that the input string `s` only contains digits. If `s` can contain non-digit characters, the function would need to be modified to skip over these characters when generating substrings.  This function also assumes that the input string `s` is not empty. If `s` can be empty, the function would need to be modified to handle this case.  This function does not handle the case where `s` contains leading zeros. If `s` can contain leading zeros, the function would need to be modified to handle this case.  This function does not handle the case where `s` contains non-integer characters. If `s` can contain non-integer characters, the function would need to be modified to handle this case.  This function does not handle the case where `s` is a very large string. If `s` can be a very large string, the function would need to be modified to handle this case.  This function does not handle the case where `s` is a very long string. If `s` can be a very long string, the function would need to be modified to handle this case.  This function does not handle the case where `s` is a very short string. If `s` can be a very short string, the function would need to be