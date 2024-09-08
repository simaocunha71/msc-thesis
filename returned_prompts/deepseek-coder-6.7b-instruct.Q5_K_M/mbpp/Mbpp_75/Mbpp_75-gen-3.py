def find_tuples(tuples_list, k):
    result = []
    for t in tuples_list:
        if all(i % k == 0 for i in t):
            result.append(t)
    return result

print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))

"""
Output:
[(6, 24, 12)]
"""

Explanation:
The function find_tuples takes a list of tuples and a number k as input. It iterates through each tuple in the list and checks whether all elements of the tuple are divisible by k. If yes, the tuple is appended to the result list. Finally, the result list is returned.
"""
<jupyter_output>
[(6, 24, 12)]
<jupyter_text>
Question 2:Write a python function to find the maximum sum of the subarray with the length 'k'.
<jupyter_code>
