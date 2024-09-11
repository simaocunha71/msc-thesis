"""
def count_Substrings(str):
    l = len(str)
    count = 0
    for i in range(l):
        for j in range(i,l):
            s = str[i:j+1]
            if len(s) == sum([int(x) for x in s]):
                count += 1
    return count

def count_Substrings(str):
    count = 0
    for i in range(1,len(str)+1):
        for j in range(len(str)):
            if len(str[j:j+i]) == sum([int(x) for x in str[j:j+i]]):
                count += 1
    return count

assert count_Substrings('112112') == 6
"""

def count_Substrings(str):
    count = 0
    for i in range(1,len(str)+1):
        for j in range(len(str)):
            if len(str[j:j+i]) == sum([int(x) for x in str[j:j+i]]):
                count += 1
    return count

assert count_Substrings('112112') == 6

# The above function is optimized to use the sum() function.
# However, it is possible to optimize it further to avoid using the sum() function.

def count_Substrings(str):
    count = 0
    for i in range(1,len(str)+1):
        for j in range(len(str)):
            s = 0
            for k in range(i):
                s += int(str[j+k])
            if s == i:
                count += 1
    return count

assert count_Substrings('112112') == 6

# Another approach is to use a loop to generate the substrings and then count the number of substrings that meet the condition.

def count_Substrings(str):
    count = 0
    for i in range(1,len(str)+1):
        for j in range(len(str)):
            s = str