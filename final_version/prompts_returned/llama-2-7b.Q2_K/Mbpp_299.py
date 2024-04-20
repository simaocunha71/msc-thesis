"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""
import operator
from functools import reduce
def max_aggregate(tuples):
    list = [reduce(operator.mul, tuple,0)]
    for elem in tuples:
        lst=tuple(element*elem.score for element in elem.members)
        if lst>list[-1]:
            list.appendleft(lst)
    list=[item for item,i in zip(list[::-1],range(len(list[0])))]
    return max(list) if type(list[-1])==int else list[-1]
# output:
# max_aggregate([('Sabah Colley',84),('Juan Whelan',90),('Peter Nichols',7),('Sabah Colley',88),('Sabah Colley',84)])==(268, 132, 7)
