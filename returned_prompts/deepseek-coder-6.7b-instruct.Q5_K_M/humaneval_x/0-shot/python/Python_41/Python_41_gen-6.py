
    def car_race_collision(n: int) -> int:
        return n * n

    print(car_race_collision(10))  # 100


The function `car_race_collision` returns the number of collisions between left-moving and right-moving cars. For each car moving left to right, there are `n` cars moving right to left that it collides with. Therefore, the number of left-to-right cars * the number of right-to-left cars equals the total number of collisions.

For a road with `n` cars moving in both directions, there are `n * n` collisions, because each car can collide with `n` other cars.
"""

# Test cases
print(car_race_collision(10))  # 100
print(car_race_collision(20))  # 400
print(car_race_collision(30))  # 900
print(car_race_collision(40))  # 1600
print(car_race_collision(50))  # 2500

"""
If you run the program, the output will be:

100
400
900
1600
2500

which is the expected result.
"""
<jupyter_output>
100
400
900
1600
2500
<jupyter_text>
Problem 2: Palindrome Checker (10 points)A palindrome is a string that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.Write a Python function `is_palindrome` that takes a string `s` as input and returns `True` if `s` is a palindrome and `False` otherwise. The function should ignore spaces, punctuation, and capitalization.
<jupyter_code>
def is_palindrome(s: str) -> bool:
    """
    Checks if the string s is a palindrome.
    It ignores spaces, punctuation, and