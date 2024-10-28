```
def max_aggregate(lst):
    aggregate = {}
    for name, score in lst:
        if name in aggregate:
            aggregate[name] += score
        else:
            aggregate[name] = score
    return max(aggregate.items(), key=lambda x: x[1])
```



The function `max_aggregate` takes a list of tuples as input, where each tuple contains a name and a score. It first initializes an empty dictionary `aggregate` to store the aggregate score for each name. Then, it iterates over the input list. For each tuple, if the name is already in the dictionary, it adds the score to the existing value; otherwise, it adds the name to the dictionary with the score as its value. Finally, it returns the tuple with the maximum aggregate score using the built-in `max` function with a lambda function as the key. This lambda function returns the value of each item in the dictionary, which is the aggregate score. The `max` function then returns the item with the maximum value, which is the tuple with the maximum aggregate score.