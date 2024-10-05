    return [abs(a-b) if a!=b else 0 for a,b in zip(game,guess)]


Explanation:
The task is to create a function that compares the scores and guesses of a number of matches and returns an array of the same length denoting how far off each guess was.

The function `compare(game,guess)` takes two arrays of scores and guesses of equal length as input. It then uses a list comprehension to iterate over the input arrays and calculate the absolute difference between the score and the guess for each match. If the guess is correct (i.e., the score and the guess are equal), the value is 0; otherwise, the value is the absolute difference between the score and the guess.

The function uses the built-in `zip` function to iterate over the input arrays in parallel. The `abs` function is used to calculate the absolute difference between the score and the guess.

For example, if the input arrays are `[1,2,3,4,5,1]` and `[1,2,3,4,2,-2]`, the function will return `[0,0,0,0,3,3]`, indicating that the guesses were correct for the first four matches and off by 3 and 3 for the last two matches. Similarly, if the input arrays are `[0,5,0,0,0,4]` and `[4,1,1,0,0,-2]`, the function will return `[4,4,1,0,0,6]`, indicating that the guesses were off by 4 and 4 for the first two matches, by 1 for the third match, and by 6 for the last match.