
def fix_spaces(text):
    result = []
    space_counter = 0
    for c in text:
        if c == ' ':
            space_counter += 1
            if space_counter == 2:
                result.append('-')
                space_counter = 1
            elif space_counter > 2:
                continue
        else:
            if space_counter > 0:
                result.append('_')
                space_counter = 0
            result.append(c)
    return ''.join(result)

print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example  3"))
<jupyter_output>
Example
Example_1
_Example_2
_Example-3
<jupyter_text>
Question 2Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i. Solve it without using division and in O(n) time.Example:```python[1, 2, 3, 4, 5] => [120, 60, 40, 30, 24]```
<jupyter_code>
