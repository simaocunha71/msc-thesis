
def rotate_right(lst, k):
    return lst[-k:] + lst[:-k]

print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))

"""
This solution works by first slicing the list at the index -k and taking the last k elements and the rest of the elements. 
Then it concatenates these two slices in reverse order to get the rotated list.
"""

# Another solution:

def rotate_right(lst, k):
    for _ in range(k):
        lst = [lst[-1]] + lst[:-1]
    return lst

print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))

"""
This solution works by continuously moving the last element to the front of the list, and repeating this process k times.
"""
<jupyter_output>
[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
<jupyter_text>
