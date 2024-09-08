def max_aggregate(lst):
    scores = {}
    for name, score in lst:
        if name in scores:
            scores[name] += score
        else:
            scores[name] = score
    max_name = max(scores, key=scores.get)
    return (max_name, scores[max_name])

print(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))

"""
In this function, we first create a dictionary where the keys are the names and the values are the sum of the scores for each name. Then we find the name with the maximum value in the dictionary and return it along with its score.
"""
<jupyter_output>
('Juan Whelan', 212)
<jupyter_text>
Problem 3
<jupyter_code>
