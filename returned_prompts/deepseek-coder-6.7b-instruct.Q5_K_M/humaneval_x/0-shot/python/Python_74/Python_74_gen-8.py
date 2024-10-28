
def total_match(lst1, lst2):
    total_chars1 = sum(len(s) for s in lst1)
    total_chars2 = sum(len(s) for s in lst2)
    if total_chars1 < total_chars2:
        return lst1
    elif total_chars2 < total_chars1:
        return lst2
    else:
        return lst1

print(total_match([], []))  # ➞ []
print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # ➞ ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # ➞ ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # ➞ ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5']))  # ➞ ['4']

In this solution, I calculate the total number of characters in each list using list comprehension and the built-in sum function. If the total number of characters in lst1 is less than the total number of characters in lst2, I return lst1. If the total number of characters in lst2 is less than the total number of characters in lst1, I return lst2. If the totals are equal, I return lst1 as required.

The time complexity of this solution is O(n) because we iterate over each string in each list once. The space complexity is O(1) because we only store the total number of characters in each list and don't use any additional data structures.
