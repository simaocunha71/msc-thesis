
def index_minimum(lst):
    lst.sort(key=lambda x: x[1])
    return lst[0][0]

print(index_minimum([('Rash', 143),  ('Manjeet', 200),  ('Varsha', 100)]))

"""
Explanation:
This function works by sorting the input list of tuples by the second element of each tuple (x[1]) using the built-in sort() function with a lambda function as the key. This sorts the tuples in ascending order based on the second element. 
The result is a sorted list of tuples where the tuples are sorted in order of increasing second element. The first element of the first tuple in the sorted list, which has the smallest second element, is returned.
"""
<jupyter_output>
Varsha
<jupyter_text>
