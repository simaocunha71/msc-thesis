
def combinations_list(lst):
    results = [[]]
    for i in range(len(lst)):
        results.extend([subset + [lst[i]] for subset in results])
    return results

print(combinations_list(['orange', 'red', 'green', 'blue']))

"""
Explanation:

This function uses a technique called list comprehension. It starts by creating a list with an empty subset, which are all possible subsets of an empty set. Then it iterates over the elements of the given list, adding each one to each of the existing subsets. This expands the list of subsets to include all possible subsets that include the current element.
"""

# Test case
print(combinations_list(['orange', 'red', 'green', 'blue']) == [
    [], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']
])
<jupyter_output>
[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
True
<jupyter_text>
Question 3:  Write a Python function to find all occurrences of a substring in a given string.
<jupyter_code>
def find_occurrences(string, substring):
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            count += 1
            start = pos + 1
        else:
            break
   