
def Find_Max_Length(list_):
    return max(len(sublist) for sublist in list_)

assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4

# Solution 2:

def Find_Max_Length(list_):
    max_length = 0
    for sublist in list_:
        if len(sublist) > max_length:
            max_length = len(sublist)
    return max_length

assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4

# Solution 3:

def Find_Max_Length(list_):
    return max(len(max(sublist, key=len)) for sublist in list_)

assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4

# Solution 4:

def Find_Max_Length(list_):
    max_length = -1
    for sublist in list_:
        for item in sublist:
            if len(str(item)) > max_length:
                max_length = len(str(item))
    return max_length

assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 1

# Solution 5:

def Find_Max_Length(list_):
    return max(len(str(item)) for sublist in list_ for item in sublist)

assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 1

# Solution 6:

def Find_Max_Length(list_):
    return len(str(max(max(sublist, key=len) for sublist in list_)))

assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 1

# Solution 7:

def Find_Max_Length(list_):
    return len(max(str(i) for sublist in list_ for i in