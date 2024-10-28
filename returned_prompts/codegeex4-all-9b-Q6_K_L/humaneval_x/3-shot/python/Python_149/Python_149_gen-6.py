    # First, delete all strings with odd lengths
    lst = [word for word in lst if len(word) % 2 == 0]

    # Sort the list by length of each word
    lst.sort(key=len)

    # Sort the list alphabetically
    lst.sort()

    return lst

