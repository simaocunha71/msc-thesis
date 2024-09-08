
def cummulative_sum(tuple_list):
    sum = 0
    for tup in tuple_list:
        for num in tup:
            sum += num
    return sum

print(cummulative_sum([(1, 3),  (5, 6, 7),  (2, 6)])) # should return 30

"""
This function works by iterating through each tuple in the given list. 
Then it iterates through each number in the tuple. 
Adding each number to the sum variable.
"""
<jupyter_output>
30
<jupyter_text>
Q2:
<jupyter_code>
