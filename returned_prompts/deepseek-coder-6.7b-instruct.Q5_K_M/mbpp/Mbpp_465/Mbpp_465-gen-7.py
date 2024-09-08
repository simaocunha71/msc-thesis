from collections import Counter

def most_common(l):
    return Counter(l).most_common(1)[0][0]

print(most_common([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]))


"""
Write a function to find the least common element in a list.
assert least