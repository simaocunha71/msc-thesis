```
def max_aggregate(tuples):
    aggregates = {}
    for name, score in tuples:
        if name in aggregates:
            aggregates[name] += score
        else:
            aggregates[name] = score
    return max(aggregates.items(), key=lambda x: x[1])
```
This function takes a list of tuples as input, where each tuple contains a name and a score. It then aggregates the scores for each name by adding them up. Finally, it returns the name with the maximum total score. The unit test `assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)` ensures that the function works correctly. 

The function uses a dictionary to store the aggregated scores. For each tuple in the input list, it checks if the name is already in the dictionary. If it is, it adds the score to the existing total. If not, it adds the name to the dictionary with the score as the value. 

Finally, it uses the built-in `max` function with a `key` function to find the name with the maximum total score. The `key` function specifies that the maximum should be found based on the value (i.e., the total score) in each dictionary item. 

The function returns the name with the maximum total score as a tuple, along with the total score. In this case, the output would be `('Juan Whelan', 212)`, which is the name with the maximum total score. 

The time complexity of this function is O(n), where n is the length of the input list, because it iterates over the list once to aggregate the scores. The space complexity is also O(n), because in the worst case, it needs to store all the names and scores in the dictionary. 