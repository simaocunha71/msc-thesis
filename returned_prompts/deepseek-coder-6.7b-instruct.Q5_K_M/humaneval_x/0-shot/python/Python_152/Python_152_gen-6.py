
def compare(game,guess):
    return [abs(g - x) for x, g in zip(game, guess)]

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) # -> [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) # -> [4,4,1,0,0,6]

# Here we use list comprehension and the built-in abs function to calculate the absolute difference 
# between each pair of scores from the game and guess arrays. We use the zip function to iterate over 
# the two arrays simultaneously.
<jupyter_output>
<empty_output>
<jupyter_text>
9. Write a python function to check if a number is prime or not.
<jupyter_code>
