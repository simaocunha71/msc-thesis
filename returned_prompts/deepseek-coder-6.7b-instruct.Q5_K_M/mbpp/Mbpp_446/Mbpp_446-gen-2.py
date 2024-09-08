def count_Occurrence(tup, lst):
    count = 0
    for i in lst:
        count += tup.count(i)
    return count

print(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] )) # Output: 3


"""
Explanation:
In the function, we are iterating over each element in the list and then using the count method on the tuple to get the count of that element. We add all these counts and return the total count.
"""
<jupyter_output>
3
<jupyter_text>
Question 2:
<jupyter_code>
