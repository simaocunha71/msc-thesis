
def index_multiplication(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        if type(tup1[i]) == tuple and type(tup2[i]) == tuple:
            result.append(tuple(x * y for x, y in zip(tup1[i], tup2[i])))
        else:
            result.append(tup1[i] * tup2[i])
    return tuple(result)

print(index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))))

"""
Explanation:
The function index_multiplication takes in two tuples. It uses a for loop to iterate through the elements of each tuple. If the element is a tuple itself, it performs element-wise multiplication and appends the result to a list. If the element is not a tuple, it multiplies it directly and appends the result to the list. Finally, it returns the result as a tuple.
"""
<jupyter_output>
((6, 21), (12, 45), (2, 9), (7, 30))
<jupyter_text>
Question 2:
<jupyter_code>
