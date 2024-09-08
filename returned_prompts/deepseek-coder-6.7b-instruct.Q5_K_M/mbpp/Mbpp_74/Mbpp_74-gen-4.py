def is_samepatterns(colors, patterns):
    color_pattern = {}
    pattern_color = {}
    for color, pattern in zip(colors, patterns):
        if color in color_pattern and color_pattern[color] != pattern:
            return False
        if pattern in pattern_color and pattern_color[pattern] != color:
            return False
        color_pattern[color] = pattern
        pattern_color[pattern] = color
    return True

print(is_samepatterns(["red","green","green"], ["a",  "b", "b"]))

# Output: True

Explanation:
The function is_samepatterns(colors, patterns) takes two arguments, a list of colors and a list of patterns. It returns True if the colors and patterns follow each other in the same order, else it returns False.

The function works by iterating over the two lists simultaneously using the zip function. It checks if the current color already has a pattern that is different from the current pattern, or if the current pattern already has a color that is different from the current color. If either of these conditions is true, it returns False. Otherwise, it adds the color-pattern pair and the pattern-color pair to their respective dictionaries, and continues to the next iteration.

If the function successfully iterates over all the pairs without returning False, it returns True, indicating that the colors and patterns follow each other in the same order.

The test case provided returns True, indicating that the colors and patterns follow each other in the same order.
"""

