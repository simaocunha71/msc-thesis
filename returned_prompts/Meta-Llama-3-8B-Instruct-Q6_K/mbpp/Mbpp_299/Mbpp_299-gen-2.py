```
def max_aggregate(tuples):
    aggregated = {}
    for name, score in tuples:
        if name in aggregated:
            aggregated[name] += score
        else:
            aggregated[name] = score
    return max(aggregated.items(), key=lambda x: x[1])
```





This function takes a list of tuples as input, where each tuple contains a name and a score. It then aggregates the scores for each name and returns the name with the maximum aggregate score. 

The unit test `assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)` ensures that the function correctly aggregates the scores and returns the name with the maximum aggregate score.

The function works by first initializing an empty dictionary `aggregated`. Then, it iterates over the input list of tuples. For each tuple, it checks if the name is already in the `aggregated` dictionary. If it is, it adds the score to the existing aggregate for that name. If it's not, it adds the name to the dictionary with the score as the initial aggregate. Finally, it returns the name with the maximum aggregate score by using the `max` function with a `key` function that returns the aggregate score for each name.