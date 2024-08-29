def max_aggregate(lst):
    name_score_dict = {}
    for name, score in lst:
        if name in name_score_dict:
            name_score_dict[name] += score
        else:
            name_score_dict[name] = score
    max_score = max(name_score_dict.values())
    max_aggregate_name = [k for k, v in name_score_dict.items() if v == max_score]
    return (max_aggregate_name[0], max_score)

print(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))

"""
This function works by first creating a dictionary where the keys are the names and the values are the sums of their respective scores. It then finds the maximum score and returns the name associated with this score.
"""

"""
Output:
('Juan Whelan', 212)
"""
<jupyter_output>
('Juan Whelan', 212)
<jupyter_text>
Question 2 (20 points)Given a list of tuples, where each tuple contains two elements: a name and a numeric score. Write a function that returns the name(s) with the maximum score. If there are multiple people with the maximum score, return all of their names as a list.
<jupyter_code>
# Your code here
def max_score(lst):
    max_score = max(score for name, score in lst)
    return [name for name, score in lst if score == max_score]

print(max_score([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]))
<jupyter_output>
['Juan Whelan', 'Sabah Colley']
<jupyter_text>
Question 3 (2