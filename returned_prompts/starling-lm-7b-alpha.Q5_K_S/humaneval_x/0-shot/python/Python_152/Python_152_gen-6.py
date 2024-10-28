
# The first array represents the scores of the game, and the second array represents the guesses.

def compare(game,guess):
    result = []
    for i in range(len(game)):
        result.append(abs(game[i]-guess[i]))
    return result



# The above function takes two arrays as input and returns an array of the same length.
# Each value of this array represents how far off the guess was, which is the absolute
# difference between the guess and the score.



# To calculate the absolute difference, we use the abs() function, which returns the absolute value of a number.

# The range function is used to loop over the indices of the game array. We use the range() function with the len(game) as the argument,
# which returns a sequence of numbers starting from 0 and ending at the length of the game array minus 1.
# This way, we can iterate through all the indices of the game array and compare the corresponding values of the game and guess arrays.

# The append() function is used to add the absolute difference between the guess and the score to the result array.

# Finally, we return the result array, which contains the absolute differences between the guesses and the scores for each match.



# The time complexity of this function is O(n), where n is the length of the game and guess arrays. This is because we only need to iterate through the arrays once to calculate the absolute differences.

# The space complexity is also O(n), as we create a result array of the same length as the game and guess arrays to store the absolute differences.



# In the given examples, the first example shows that the guesses are correct for all matches, so the result array is [0,0,0,0,3,3].
# The second example shows that the guesses are not correct for some matches, so the result array is [4,4,1,0,0,6].



# These two examples demonstrate the functionality of the function and its ability to correctly calculate the absolute differences between the guesses and the scores for each match.































