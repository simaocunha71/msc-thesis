

    def count_chars(s: str):
        """
        Count the number of occurrences of each character in a string.
        """
        counts = {}
        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
        return counts

    return count_chars(s0) == count_chars(s1)

# Tests
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
<jupyter_output>
True
True
True
False
False
False
<jupyter_text>
Exercise 3: Unique SumWrite a function `unique_sum` that takes a list of integers and returns the sum of all unique integers in the list. The function should ignore any duplicate numbers when summing.
<jupyter_code>
