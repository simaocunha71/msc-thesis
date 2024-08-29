
def average_tuple(t):
    averages = []
    for i in t:
        averages.append(sum(i)/len(i))
    return averages

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))

"""
In the function 'average_tuple', we use a for loop to iterate through each tuple in the input tuple of tuples. 
Inside the loop, we calculate the average of each tuple by dividing the sum of the elements by the length of the tuple. 
The average is then appended to the 'averages' list.
Finally, the function returns the 'averages' list.
"""
<jupyter_output>
[10.5, 42.25, 30.5, 2.5]
<jupyter_text>
Question 3
<jupyter_code>
