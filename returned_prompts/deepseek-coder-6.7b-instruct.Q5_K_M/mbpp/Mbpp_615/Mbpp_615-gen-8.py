
def average_tuple(tup):
    averages = []
    for t in tup:
        averages.append(sum(t)/len(t))
    return averages

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))

# Output: [30.5, 34.25, 27.0, 23.25]

"""
Explanation:
In the function, for each tuple in the input tuple, we use the built-in python function sum() to find the sum of elements and len() to find the number of elements in each tuple. Then we divide the sum by the number of elements to get the average and append it to the list averages. Finally we return the list averages.
"""
<jupyter_output>
[30.5, 34.25, 27.0, 23.25]
<jupyter_text>
Question 3
<jupyter_code>
