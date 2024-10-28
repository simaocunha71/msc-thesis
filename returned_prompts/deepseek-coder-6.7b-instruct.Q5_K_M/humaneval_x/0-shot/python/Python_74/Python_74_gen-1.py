
def total_match(lst1, lst2):
    sum1 = sum(len(i) for i in lst1)
    sum2 = sum(len(i) for i in lst2)
    if sum1 < sum2:
        return lst1
    elif sum1 > sum2:
        return lst2
    else:
        return lst1

print(total_match([], [])) # ➞ []
print(total_match(['hi', 'admin'], ['hI', 'Hi'])) # ➞ ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])) # ➞ ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])) # ➞ ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5'])) # ➞ ['4']

This program works by first calculating the total character count in each list using the sum() function combined with a generator expression. It then compares these totals and returns the list with the smaller total. If the totals are equal, it returns the first list.

The program then tests the function with the given examples and prints the output.

The time complexity of this program is O(n), where n is the total number of strings in both lists, as it iterates through each string once to calculate its length. The space complexity is O(1), as it uses a fixed amount of space to store the total character counts and the input lists.

Please note that the function assumes that the input lists only contain strings. If this is not the case, you may need to modify the function to handle non-string elements correctly.
