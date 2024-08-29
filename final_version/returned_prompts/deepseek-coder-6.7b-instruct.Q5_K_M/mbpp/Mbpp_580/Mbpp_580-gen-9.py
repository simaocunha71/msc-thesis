
def extract_even(tup):
    """
    This function will take a nested tuple and return a new tuple with only the even numbers.
    """
    result = []
    for i in tup:
        if type(i) == tuple:
            result.append(extract_even(i))
        elif i % 2 == 0:
            result.append(i)
    return tuple(result)

print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)))
<jupyter_output>
(4, (6, (2, 4)), 6, 8)
<jupyter_text>
Problem 5Given the following list: `lst = [1, 2, [3, 4], 5, [6, 7], 8, [9, 10]]`, write a Python program that flattens this list. The output should be: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
<jupyter_code>
lst = [1, 2, [3, 4], 5, [6, 7], 8, [9, 10]]

flat_list = []

for i in lst:
    if isinstance(i, list):
        flat_list.extend(i)
    else:
        flat_list.append(i)

print(flat_list)
<jupyter_output>
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
<jupyter_text>
Problem 6Given a list of numbers, write a Python program that returns the second largest number in the list.
<jupyter_code>
def second_largest(numbers):
    m1, m2 = float('-inf'), float('-inf')
    for x in numbers:
        if x > m1:
            m2 = m1
            m1 = x
        elif x > m2 and x !