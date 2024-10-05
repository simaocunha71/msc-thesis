    # First element will always be sorted
    if len(lst) == 1:
        return True

    # Compare first two elements
    if lst[1] <= lst[0]:
        return False

    # Check for duplicate
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return False

    # Check if last element is greater than the previous
    if lst[len(lst) - 2] <= lst[len(lst) - 1]:
        return False

    return True


# Driver code
if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    print(is_sorted(lst))







```
