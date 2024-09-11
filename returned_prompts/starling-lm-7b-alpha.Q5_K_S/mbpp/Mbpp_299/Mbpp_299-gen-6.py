"""
def max_aggregate(l):
    scores={}
    for i in l:
        if i[0] not in scores:
            scores[i[0]]=i[1]
        else:
            scores[i[0]]+=i[1]
    max_score=max(scores.values())
    for k in scores:
        if scores[k]==max_score:
            return (k,max_score)
max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])
"""

# Python Program to find maximum aggregate from the list of tuples
def max_aggregate(l):
    scores={}
    for i in l:
        if i[0] not in scores:
            scores[i[0]]=i[1]
        else:
            scores[i[0]]+=i[1]
    max_score=max(scores.values())
    for k in scores:
        if scores[k]==max_score:
            return (k,max_score)

# Driver Code
if __name__=='__main__':
    l= [('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]
    print(max_aggregate(l))





# This code is contributed by Amit Khandelwal.


# Python3 program to find the
# maximum aggregate from a list
# of tuples

# Function to calculate maximum
# aggregate from the list of
# tuples
def max_aggregate(l):
    # Dictionary to store the
    # aggregate of each person
    scores={}

    # Iterate through the given
    # list of tuples
    for i in l:
        # If the person is not
        # present in the dictionary
        # then add the aggregate
        # of the person in the
        # dictionary