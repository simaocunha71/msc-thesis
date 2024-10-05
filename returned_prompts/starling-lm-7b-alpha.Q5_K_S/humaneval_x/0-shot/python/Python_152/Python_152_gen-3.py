
def compare(game,guess):
    result = []
    for i in range(len(game)):
        result.append(abs(game[i]-guess[i]))
    return result




















```
compare([1,2,3,4,5,1],[1,2,3,4,2,-2])
```

In this code, the `compare` function takes two arrays as input: `game` and `guess`. It then iterates over the indices of the arrays using the `range` function, and for each index, it calculates the absolute difference between the corresponding elements of the `game` and `guess` arrays. The result of each calculation is appended to a new list called `result`. Finally, the function returns the `result` list.

To test the function, you can call it with example inputs like `compare([1,2,3,4,5,1],[1,2,3,4,2,-2])`. This will return the array `[0,0,0,0,3,3]`, indicating that the guesses were off by 3 points for the last two matches.

Similarly, calling `compare([0,5,0,0,0,4],[4,1,1,0,0,-2])` will return the array `[4,4,1,0,0,6]`, showing that the guesses were off by 4, 4, 1, 0, 0, and 6 points respectively.

Overall, the `compare` function provides a way to compare the accuracy of guesses made in relation to the actual scores, and returns an array of the absolute differences between the guesses and the actual scores.
```

```