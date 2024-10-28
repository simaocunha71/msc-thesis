
    negative = [num for num in lst if num < 0]
    positive = [num for num in lst if num > 0]

    if negative:
        a = max(negative)
    else:
        a = None

    if positive:
        b = min(positive)
    else:
        b = None

    return (a, b)

# Test cases
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # (None, 1)
print(largest_smallest_integers([]))  # (None, None)
print(largest_smallest_integers([0]))  # (None, None)
print(largest_smallest_integers([-2, -4, -1, -3, -5, 7]))  # (-1, 7)
print(largest_smallest_integers([2, 4, 1, 3, 5, -7]))  # (-7, 1)
print(largest_smallest_integers([-2, -4, -1, -3, -5, 0]))  # (-1, None)
<jupyter_output>
(None, 1)
(None, None)
(None, None)
(-1, 7)
(-7, 1)
(-1, None)
<jupyter_text>
Q2: Write a Python function named `average_of_three` that receives a list of three numbers and returns their average. If the list does not contain exactly three elements or any of the elements are not numbers, the function should return `None`.
<jupyter_code>
# 