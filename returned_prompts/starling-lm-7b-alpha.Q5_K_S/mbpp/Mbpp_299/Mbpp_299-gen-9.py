def max_aggregate(tuples):
    max_score, name = 0, ''
    for tup in tuples:
        name, score = tup
        if score > max_score:
            max_score = score
            name = name
    return (name, max_score)


# Test
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
print("Test Passed")




"""
The function works by first defining an initial maximum score and name. Then, it loops over all tuples. For each tuple, it unpacks the name and score. If the score is higher than the current maximum, it updates the maximum score and name. Finally, it returns the name and maximum score.
"""

"""
The code defines a function called max_aggregate that takes a list of tuples as an argument. It initializes two variables: max_score to 0 and name to an empty string. Then, it loops over all tuples in the input list. For each tuple, it unpacks the name and score using tuple assignment. It then checks if the current score is higher than the current maximum. If it is, it updates the maximum score and name. Finally, it returns a tuple containing the name with the maximum score.
"""

# Test
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
print("Test Passed")

# End

"""
The function max_aggregate takes a list of tuples as an argument. It initializes two variables: max_score to 0 and name to an empty string. Then, it loops over all tuples in the input list. For each tuple, it unpacks the name and score using tuple assignment. It then checks if the current score is higher than the current maximum. If it