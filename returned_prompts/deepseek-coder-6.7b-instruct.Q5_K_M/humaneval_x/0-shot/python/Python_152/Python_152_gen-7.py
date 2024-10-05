
def compare(game, guess):
    return [abs(g-c) for g, c in zip(game, guess)]


print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2]))  #-> [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2]))  #-> [4,4,1,0,0,6]


In this solution, we use the Python built-in function `zip` to iterate over two lists simultaneously, and the `abs` function to compute the absolute difference between the score and the guess. We use a list comprehension to return a new list with these differences.

The `zip` function is a good choice here because it allows us to iterate over the two input lists simultaneously. This makes the code easier to read and understand.

The `abs` function is used to ensure that the difference is always positive, which matches the problem description.
"""


def compare(game, guess):
    return [abs(g - c) for g, c in zip(game, guess)]


print(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]))  # -> [0, 0, 0, 0, 3, 3]
print(compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]))  # -> [4, 4, 1, 0, 0, 6]
<jupyter_output>
[0, 0, 0, 0, 3, 3]
[4, 4, 1, 0, 0, 6]
<jupyter_text>
**Note**: The `zip` function stops at the end of the shortest list. This is exactly what we want in this case, because we want to compare the scores and guesses one by one, and they both have to be of the same