    # First remove the elements of odd length
    lst = [x for x in lst if len(x) % 2 == 0]

    # Then sort the list by length of each word, and by alphabetical order
    lst.sort()
    lst.sort(key=len)

    return lst

