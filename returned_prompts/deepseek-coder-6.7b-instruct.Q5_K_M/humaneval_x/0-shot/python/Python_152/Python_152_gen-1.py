
def compare(game, guess):
    return [abs(g - h) for g, h in zip(game, guess)]

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) # [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) # [4,4,1,0,0,6]

Here, I used list comprehension to iterate over both lists simultaneously (using zip) and calculated the absolute difference between the corresponding scores and guesses. The result is a list of differences.

If you want to return the result as a dictionary, you can modify the function as follows:

```python
def compare(game, guess):
    return {f"match_{i+1}": abs(g - h) for i, (g, h) in enumerate(zip(game, guess))}
```

This will return a dictionary where the keys are match numbers (1-indexed) and the values are the differences.
'''


# 3.

'''
