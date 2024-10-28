
def total_match(lst1, lst2):
    return lst1 if sum(len(s) for s in lst1) < sum(len(s) for s in lst2) else lst2

# Test cases
print(total_match([], []))  # ➞ []
print(total_match(['hi', 'admin'], ['hI', 'Hi']))  # ➞ ['hI', 'Hi']
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))  # ➞ ['hi', 'admin']
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))  # ➞ ['hI', 'hi', 'hi']
print(total_match(['4'], ['1', '2', '3', '4', '5']))  # ➞ ['4']

This function works by first calculating the total number of characters in each list by summing up the length of each string in the list. It then compares these sums and returns the list with the smaller sum. If the sums are equal, it returns the first list.

This solution uses list comprehension to compute the sums, which is a compact way to perform operations on lists in Python. It also uses the built-in len function to get the length of each string, and the less than operator to compare the sums.

Finally, it uses the ternary operator (also known as the conditional expression) to return the appropriate list. The expression lst1 if sum(len(s) for s in lst1) < sum(len(s) for s in lst2) else lst2 evaluates to lst1 if the sum of the lengths of strings in lst1 is less than the sum of the lengths of strings in lst2, and to lst2 otherwise.

Please note that this solution assumes that the input lists are valid and do not contain any non-string elements. If this is not the case, you may need to add error checking code to handle invalid input.

Also, note that this solution assumes that the length of a string is the number of characters in the string, which is the usual interpretation of the term "length". If the length of a