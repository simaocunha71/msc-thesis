```python
def index_multiplication(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        temp = []
        for j in range(len(tup1[i])):
            temp.append(tup1[i][j]*tup2[i][j])
        result.append(tuple(temp))
    return tuple(result)

tup1 = ((1, 3), (4, 5), (2, 9), (1, 10))
tup2 = ((6, 7), (3, 9), (1, 1), (7, 3))
print(index_multiplication(tup1, tup2))
```

Output:
```python
((6, 21), (12, 45), (2, 9), (7, 30))
```

Explanation:
The function `index_multiplication` takes two tuples as inputs. It iterates over the length of the first tuple, and for each element in the tuple, it iterates over the length of that element (which is assumed to be a tuple) and multiplies the corresponding elements of the second tuple. The result is a new tuple with the multiplied values. This new tuple is appended to the `result` list, which is returned at the end.

The output of this function matches the expected output.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3
<jupyter_code>
"""
