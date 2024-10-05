
def total_match(lst1, lst2):
    sum1 = sum(len(i) for i in lst1)
    sum2 = sum(len(i) for i in lst2)
    if sum1 < sum2:
        return lst1
    elif sum1 > sum2:
        return lst2
    else:
        return lst1

print(total_match([], []))
print(total_match(['hi', 'admin'], ['hI', 'Hi']))
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))
print(total_match(['4'], ['1', '2', '3', '4', '5']))

This function works by first calculating the sum of the lengths of the strings in each list using a generator expression. It then compares these sums to determine which list has the total number of characters less than the other. It returns the list with the smaller sum. If the sums are equal, it returns the first list.

This solution assumes that the lists passed to the function are not empty, as it does not handle the case where an empty list is passed. If this is a possibility, you could add a check for this at the start of the function and return an empty list if one of the lists is empty.
