    # This is my own solution
    # lst1_even_count = sum(1 for i in lst1 if i % 2 == 0)
    # lst2_even_count = sum(1 for i in lst2 if i % 2 == 0)
    # if lst1_even_count == len(lst1) and lst2_even_count == len(lst2):
    #     return "YES"
    # return "NO"

    # This is the solution from the book
    lst1_even_count = sum(1 for x in lst1 if x % 2 == 0)
    if lst1_even_count == 0:
        return "NO"

    for i in range(len(lst1)):
        if lst1[i] % 2 == 0 and lst2[i] % 2 != 0:
            return "YES"

    return "NO"


