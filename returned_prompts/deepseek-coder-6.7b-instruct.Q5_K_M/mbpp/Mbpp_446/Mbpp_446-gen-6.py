
def count_Occurrence(tup, list_):
    count = 0
    for i in list_:
        count += tup.count(i)
    return count

print(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ))

"""
In this function, we use the count method of tuple and add up all the counts to get the total count.
"""
<jupyter_output>
3
<jupyter_text>
Question 2
<jupyter_code>
