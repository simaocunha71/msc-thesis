def find_tuples(tuples, k):
    result = []
    for t in tuples:
        if all(i % k == 0 for i in t):
            result.append(t)
    return result

print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))

"""
Output:
[(6, 24, 12)]
"""

Explanation:
In the function find_tuples, we iterate over each tuple in the list. We then use the built-in all function and the generator comprehension to check if all elements of the tuple are divisible by k. If they are, we append the tuple to our result list. Finally, we return the result list.
"""