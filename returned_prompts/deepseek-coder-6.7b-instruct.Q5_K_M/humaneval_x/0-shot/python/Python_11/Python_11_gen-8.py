from typing import List

def string_xor(a: str, b: str) -> str:
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result

print(string_tasks.string_xor('010', '110'))

This code will return '100' as output.

Here we are iterating over the two strings from the beginning, and if the bits in the strings at the same position are the same we append '0' to the result, otherwise we append '1'. This gives us the binary XOR of the two strings.

If you run the code with the example inputs, you will get the expected output.

The time complexity of this code is O(n) where n is the length of the input strings, because we are looping over the strings once. The space complexity is also O(n) because we are storing the result in a new string.
"""

# Tests:
print(string_xor('010', '110'))  # should return '100'
print(string_xor('101', '001'))  # should return '100'
print(string_xor('111', '111'))  # should return '000'
print(string_xor('000', '111'))  # should return '111'
<jupyter_output>
100
100
000
111
<jupyter_text>
**Task 2:**Create a function that takes an input list of strings and returns the strings in the order of increasing length. The function should return a list of strings, and if two strings have the same length, the string that comes first in the original list should come first in the returned list.
<jupyter_code>
# Code:

def order_strings(lst: List[str]) -> List[str]:
    return sorted(lst, key=len)

# Tests:
print(order_strings(['abc', 'de',