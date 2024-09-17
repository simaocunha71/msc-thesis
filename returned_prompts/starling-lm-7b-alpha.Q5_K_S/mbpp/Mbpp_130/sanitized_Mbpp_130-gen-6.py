def max_occurrences(lst):
    dictionary = {}
    for i in lst:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    maximum = 0
    max_key = 0
    for i in dictionary:
        if dictionary[i] > maximum:
            maximum = dictionary[i]
            max_key = i
    return max_key