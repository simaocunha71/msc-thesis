def find_tuples(tuples_list, k):
    return [t for t in tuples_list if all(i % k == 0 for i in t)]

print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))  # [(6, 24, 12)]

"""
Explanation:
In this function, we use a list comprehension to go through each tuple in the list. For each tuple, we use the all() function to check if all elements are divisible by k (i % k == 0). If yes, we include the tuple in the result list.
"""


