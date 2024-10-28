def number_of_substrings(string):
    length = len(string)
    if length == 0:
        return 0
    else:
        count = 0
        for i in range(length):
            for j in range(i+1, length+1):
                count += 1
        return count