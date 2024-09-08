Here is the Python function for the problem:

```python
def max_aggregate(lst):
    scores = {}
    for name, score in lst:
        if name in scores:
            scores[name] += score
        else:
            scores[name] = score
    max_score = max(scores.values())
    max_scorer = [name for name, score in scores.items() if score == max_score]
    return (max_scorer[0], max_score)

print(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))
```

In this function, we first calculate the scores for each player by summing up the scores for each player. Then, we find the maximum score and return the player with the maximum score, along with their maximum score.
"""

# Test Cases
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
assert max_aggregate([('Alice',80),('Bob',100),('Charlie',90),('Alice',70),('Bob',80)])==('Bob', 180)
assert max_aggregate([('David',90),('Emily',95),('Frank',85),('David',75),('Emily',80)])==('David', 165)
assert max_aggregate([('George',75),('Hannah',80),('Ivan',90),('Hannah',70),('Ivan',80)])==('Ivan', 170)
"""

# Expected Output
('Juan Whelan', 212)
('Bob', 180)
('David', 165)
('Ivan', 170)