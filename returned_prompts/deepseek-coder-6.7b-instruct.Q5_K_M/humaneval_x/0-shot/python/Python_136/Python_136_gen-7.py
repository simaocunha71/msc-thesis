
    neg = [x for x in lst if x < 0]
    pos = [x for x in lst if x > 0]

    if neg:
        a = max(neg)
    else:
        a = None

    if pos:
        b = min(pos)
    else:
        b = None

    return (a, b)
<jupyter_output>
<empty_output>
<jupyter_text>
Explanation:The function largest_smallest_integers takes a list lst as an argument. It first creates two lists, neg and pos, that store the negative and positive integers from lst, respectively. Then it checks whether these lists are empty. If not, it assigns the largest negative integer to a and the smallest positive integer to b. If the lists are empty, it assigns None to a and b. Finally, it returns a tuple (a, b).  Test Cases:
<jupyter_code>
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) # should return (None, 1)
print(largest_smallest_integers([])) # should return (None, None)
print(largest_smallest_integers([0])) # should return (None, None)
<jupyter_output>
(None, 1)
(None, None)
(None, None)
<jupyter_text>
Question 2: Write a Python function that returns a list of the unique elements in a list.
<jupyter_code>
