The function `compare(game,guess)` compares the scores in the `game` list with the guesses in the `guess` list.
It returns a list of the same length as `game` and `guess`, where each element is the absolute difference between the corresponding scores and guesses if the guess was not correct, and 0 if the guess was correct.

Here is the Python code for the function:

```
def compare(game,guess):
    return [abs(g-s) if g!=s else 0 for g,s in zip(game,guess)]
```

This function uses a list comprehension to create the result list. The `zip(game,guess)` function is used to pair up the corresponding elements from the `game` and `guess` lists. The `abs(g-s) if g!=s else 0` expression is used to calculate the absolute difference between the score and the guess if the guess was not correct, and 0 if the guess was correct. The `abs` function is used to get the absolute value of the difference. The `if g!=s else 0` part is a conditional expression that returns 0 if the guess was correct (i.e., `g` equals `s`), and the absolute difference otherwise. The `zip` function is used to iterate over the pairs of elements from the two lists in parallel. The list comprehension then uses these pairs to create the result list.