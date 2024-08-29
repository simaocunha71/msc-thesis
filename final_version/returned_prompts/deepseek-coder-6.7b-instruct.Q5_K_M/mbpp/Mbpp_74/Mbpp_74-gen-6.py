
def is_samepatterns(color_array, pattern_array):
    color_dict = {}
    pattern_dict = {}

    for i in range(len(color_array)):
        if color_array[i] not in color_dict:
            color_dict[color_array[i]] = [i]
        else:
            color_dict[color_array[i]].append(i)

    for i in range(len(pattern_array)):
        if pattern_array[i] not in pattern_dict:
            pattern_dict[pattern_array[i]] = [i]
        else:
            pattern_dict[pattern_array[i]].append(i)

    color_values = list(color_dict.values())
    pattern_values = list(pattern_dict.values())

    return color_values == pattern_values

# Test Cases
print(is_samepatterns(["red","green","green"], ["a",  "b", "b"]))  # should return True
print(is_samepatterns(["red","green","green"], ["a",  "b", "b", "b"]))  # should return False

"""
Explanation:
In the first test case, the color patterns ["red", "green", "green"] correspond to the pattern ["a", "b", "b"]. Therefore, the function returns True.

In the second test case, the color patterns ["red", "green", "green"] correspond to the pattern ["a", "b", "b", "b"]. Because the pattern has an extra "b", it does not correspond to the colors, so the function returns False.
"""
<jupyter_output>
True
False
<jupyter_text>
Problem 2:
<jupyter_code>
