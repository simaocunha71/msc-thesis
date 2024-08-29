def perfect_squares(start, end):
    return [i * i for i in range(start, end+1) if int(i**0.5)**2 == i * i]

print(perfect_perfect_squares(1,30))

"""
The above code works by using a list comprehension. It creates a list of squares by iterating over all the integers between the start and end (inclusive).

It checks if the square root of each integer is an integer (i.e., it is a perfect square) by comparing the square of the integer's square root to the integer itself. If they are equal, then the integer is a perfect square, and it is included in the list.

Finally, it returns the list of perfect squares.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
**Problem 2:**
<jupyter_code>
