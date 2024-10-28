
def compare(game, guess):
    return [abs(g - h) for g, h in zip(game, guess)]

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) #[0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) #[4,4,1,0,0,6]

# The zip function combines the two lists so that we can compare the corresponding elements. 
# The abs function gives the absolute value of the difference, which is the amount of error in the guess. 
# If the guess is correct, the abs function will return 0.

