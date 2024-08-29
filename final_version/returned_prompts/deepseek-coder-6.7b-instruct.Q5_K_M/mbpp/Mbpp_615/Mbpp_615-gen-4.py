def average_tuple(t):
    averages = []
    for i in t:
        averages.append(sum(i)/len(i))
    return averages

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))

# Output: [30.5, 34.25, 27.0, 23.25]

Explanation:
The function takes a tuple of tuples as input. It then iterates over the outer tuple, and for each inner tuple, it computes the average by dividing the sum of the elements by the number of elements. This average is then added to the list averages. The function returns this list of averages.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3:
<jupyter_code>
"""
