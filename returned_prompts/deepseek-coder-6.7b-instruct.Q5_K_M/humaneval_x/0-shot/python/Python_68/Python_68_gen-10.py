
def pluck(arr):
    if not arr: return []
    even_values = [(v, i) for i, v in enumerate(arr) if v % 2 == 0]
    if not even_values: return []
    even_values.sort()
    return [even_values[0][0], even_values[0][1]]

print(pluck([4,2,3])) # [2, 1]
print(pluck([1,2,3])) # [2, 1]
print(pluck([])) # []
print(pluck([5, 0, 3, 0, 4, 2])) # [0, 1]


"""
This solution works by first checking if the input array is empty, if it is it returns an empty list.
It then creates a list of tuples where each tuple contains the value and index of each even number in the array.
If there are no even numbers it will return an empty list.
The list of tuples is then sorted by value and then index.
Finally, it returns the smallest value and its index as a list.
"""


"""
The time complexity of this solution is O(n log n) because of the sort operation. The space complexity is O(n) because of the list of tuples.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Q2:
<jupyter_code>
