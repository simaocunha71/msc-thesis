
def vowels_count(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


# Test Cases
from test import Test

test = Test()
test.assert_equals(vowels_count("abcde"), 2)
test.assert_equals(vowels_count("ACEDY"), 3)
test.assert_equals(vowels_count("Y"), 1)
test.assert_equals(vowels_count(""), 0)
test.assert_equals(vowels_count("abc"), 1)
test.assert_equals(vowels_count("a"), 1)
test.run()

```
