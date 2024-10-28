    # Step 1. Create a new list that contains the entries of the original list that will be modified based on the rules of the function.
    modified_lst = []
    for index, value in enumerate(lst):
        if index % 3 == 0:
            modified_lst.append(value ** 3)
        elif index % 4 == 0:
            modified_lst.append(value ** 2)
        else:
            modified_lst.append(value)

    # Step 2. Return the sum of the modified_list
    return sum(modified_lst)
