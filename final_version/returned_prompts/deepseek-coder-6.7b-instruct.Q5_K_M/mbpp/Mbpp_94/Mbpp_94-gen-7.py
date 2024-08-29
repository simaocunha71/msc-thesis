def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]

print(index_minimum([('Rash', 143),  ('Manjeet', 200),  ('Varsha', 100)]))

"""
This function works by using the built-in Python function min(), which returns the smallest item in an iterable or the smallest of two or more arguments. The optional key argument specifies a function of one argument that is used to extract a comparison key from each element in the iterable. The min() function returns the item that has the smallest key value.

In this case, the key function is lambda x: x[1], which means that the key to compare is the second element of each tuple (x[1]). The min() function returns the tuple with the smallest second element, and the [0] at the end of the function returns the first element of this tuple.
"""
<jupyter_output>
Varsha
<jupyter_text>
Question 2
<jupyter_code>
"""
