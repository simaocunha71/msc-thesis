
Here is a Python solution for this problem:

```python
def count_upper(s):
    count = 0
    vowels = "AEIOU"
    for i in range(0, len(s), 2):
        if s[i] in vowels and s[i].isupper():
            count += 1
    return count
```

In this solution, we define a function `count_upper` that takes a string `s` as input. We initialize a counter variable `count` to keep track of the number of uppercase vowels in even indices. We also define a string `vowels` that contains all the uppercase vowels.

Next, we use a for loop to iterate over the indices of the string `s` with a step of 2 (to only consider even indices). Inside the loop, we check if the character at the current index is an uppercase vowel using the `in` operator and the `isupper()` method. If it is, we increment the `count` variable.

Finally, we return the value of `count`, which represents the number of uppercase vowels in even indices in the input string `s`.

You can test this solution with the provided examples:

```python
print(count_upper('aBCdEf'))  # Output: 1
print(count_upper('abcdefg'))  # Output: 0
print(count_upper('dBBE'))  # Output: 0
```

The expected outputs are correctly printed by the `print` statements.

In the first example, the string 'aBCdEf' has one uppercase vowel 'B' at the even index 1. So, the function returns 1.

In the second example, the string 'abcdefg' does not have any uppercase vowels at even indices. So, the function returns 0.

In the third example, the string 'dBBE' also does not have any uppercase vowels at even indices. So, the function returns 0.

I hope this helps! Let me know if you have any more questions.

```python

```

Here is a Python solution for this problem:

```