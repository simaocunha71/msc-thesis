
def compare(game, guess):
    return [abs(g - x) for x, g in zip(game, guess)]

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) # -> [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) # -> [4,4,1,0,0,6]

# The function uses a list comprehension and the built-in zip function to iterate over both input lists simultaneously.
# For each pair of corresponding elements, it calculates the absolute difference between them using abs(g - x) and returns a list of these differences.

# The zip function takes two (or more) iterable arguments and returns an iterator that generates tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted.

# The list comprehension is a compact way of creating a new list by performing an operation on each item in an existing list. In this case, it's creating a new list by taking the absolute difference between the corresponding elements in the input lists.

# The abs function returns the absolute value of a number. The absolute value is the value without regard to direction, so it's always non-negative.

# The - operator returns the difference between two numbers, so if the guess is greater than the actual score, it returns a positive number, and if the guess is less than the actual score, it returns a negative number.

# Finally, the function returns the list of differences.
<jupyter_output>
<empty_output>
<jupyter_text>
3. Write a function that can read a string and return the number of digits in it.
<jupyter_code>
