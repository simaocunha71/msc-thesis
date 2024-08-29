def list_split(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

print(list_split(['a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n'],3))

# The function works by using a list comprehension to generate new lists. The range function is used with a step of n to create the new lists. Each new list contains elements from the original list at indices i, i+1, i+2, ..., up to a maximum of len(lst).
<jupyter_output>
[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
<jupyter_text>
Problem 2:Write a function that takes in a list of tuples and returns the list sorted in ascending order by the last element of each tuple.
<jupyter_code>
