def is_samepatterns(colors, patterns):
    return len(set(zip(colors, patterns))) == 1

print(is_samepatterns(["red","green","green"],  ["a",  "b",  "b"]))

"""
The function is_samepatterns takes two lists as input - one for colors and one for patterns. It returns True if the colors and patterns follow the same sequence and False otherwise. It does this by creating a set of the zipped lists of colors and patterns. A set in Python is an unordered collection of items where every item is unique. So, if the length of the set is 1, it means that all colors and patterns follow the same sequence, so the function returns True. If the length of the set is more than 1, it means that the colors and patterns do not follow the same sequence, so the function returns False.
"""

# Method 2
def is_samepatterns(colors, patterns):
    return all(color == patterns[0] for color, pattern in zip(colors, patterns))

print(is_samepatterns(["red","green","green"],  ["a",  "b",  "b"]))

"""
The function is_samepatterns takes two lists as input - one for colors and one for patterns. It returns True if the colors and patterns follow the same sequence and False otherwise. It does this by checking if all the pairs of colors and patterns are the same. If they are, the function returns True. If there is at least one pair that is not the same, the function returns False.
"""
<jupyter_output>
True
True
<jupyter_text>
