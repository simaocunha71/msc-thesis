
def compare(game, guess):
    return [abs(i-j) for i, j in zip(game, guess)]

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) # [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) # [4,4,1,0,0,6]

This problem is quite straightforward. We can use Python's built-in `zip()` function to iterate over the two given lists simultaneously and calculate the absolute difference between corresponding elements. We can use list comprehension to do this in a single line of code.

This solution has a time complexity of O(n), where n is the length of the input lists.
"""

# Alternative Solution using for loop

def compare(game, guess):
    result = []
    for g, p in zip(game, guess):
        result.append(abs(g - p))
    return result

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) # [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) # [4,4,1,0,0,6]
<jupyter_output>
[0, 0, 0, 0, 3, 3]
[4, 4, 1, 0, 0, 6]
<jupyter_text>
Problem 3:
<jupyter_code>
"""
