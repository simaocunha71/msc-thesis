def surface_Area(base_edge, height):
    base_Area = base_edge ** 2
    side_Area = 0.5 * 4 * base_edge * height
    return round(base_Area + side_Area, 2)

print(surface_Area(3,4))

#Output: 33.0
<jupyter_output>
33.0
<jupyter_text>
13. Write a Python function to check whether a string is a pangram or not. Note: Pangrams are words or sentences containing every letter of the alphabet at least once. The most widely known pangram is "The quick brown fox jumps over the lazy dog".
<jupyter_code>
