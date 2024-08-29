def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]

# Test
print(index_minimum([('Rash', 143),  ('Manjeet', 200),  ('Varsha', 100)]))  # should return 'Varsha'

# The function works by using the min function with a key that returns the second element of each tuple. The min function then returns the tuple with the smallest second element. The [0] index at the end gets the first element of this tuple.

# The min function in Python works by comparing all the elements and returning the smallest one. If you provide a key function, it will use that function to compare the elements instead. In this case, the key function is lambda x: x[1], which means it will compare the second elements of the tuples instead of the tuples themselves.
<jupyter_output>
Varsha
<jupyter_text>
Q2. Write a function that returns the most frequent element in a list.
<jupyter_code>
