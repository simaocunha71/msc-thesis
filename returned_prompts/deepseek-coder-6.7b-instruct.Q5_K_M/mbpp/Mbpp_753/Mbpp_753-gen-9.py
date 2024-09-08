def min_k(lst, k):
    return sorted(lst, key = lambda x: x[1])[:k]

print(min_k([('Manjeet', 10),  ('Akshat', 4),  ('Akash', 2),  ('Nikhil', 8)], 2))  # [('Akash', 2),  ('Akshat', 4)]

"""
Explanation:
The function min_k takes in a list of tuples and an integer k. It sorts the list of tuples in ascending order based on the second element of the tuples (i.e., the numbers in the tuples) and returns the first k tuples.

In the test case, the function is asked to find the two tuples with the smallest second elements. The function does this correctly and returns [('Akash', 2),  ('Akshat', 4)] as expected.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2 (20 Points)
<jupyter_code>
