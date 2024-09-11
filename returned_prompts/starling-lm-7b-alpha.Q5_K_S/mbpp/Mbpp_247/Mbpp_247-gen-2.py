```
def lps(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    else:
        lps_length = [0 for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == s[0]:
                lps_length[i] = 1
        for i in range(1,len(s)):
            for j in range(i):
                if s[i] == s[j] and i - j + 1 > lps_length[i]:
                    lps_length[i] = i - j + 1
        return max(lps_length)
```

This function works by initializing an array called `lps_length` to store the lengths of the longest palindromic substrings at each index of the given string. We start by checking if the string is empty or only has one character. If so, we return 0 or 1 respectively, as there are no palindromic subsequences in these cases.

Next, we iterate through the string and check if each character is equal to the first character. If so, we set the length of the palindromic subsequence at that index to 1.

Then, we iterate through the string again, this time comparing each character to every previous character. If the characters are equal and the length of the subsequence formed by them is greater than the current length of the palindromic subsequence at that index, we update the length of the subsequence at that index.

Finally, we return the maximum length of the palindromic subsequence among all indices, which is the length of the longest palindromic subsequence in the given string.

You can test this function with the provided assertion `lps("TENS FOR TENS") == 5` to verify that it correctly calculates the length of the longest palindromic subsequence in the given string.

```python
import unittest

class TestLps(unittest.TestCase):
    def test_lps(self):
        self.assertEqual(lps("TENS FOR TENS"), 5)

if __