def intersperse(s1, s2):
    result = []
    for i in range(len(s1)):
        result.append(s2[i%len(s2)])
        result.append(s1[i])
    return ''.join(result)


"""
Write a function that takes a string and returns a dictionary with the number of times each character appears in the string.

assert count_characters('hello, world') == {'h': 1, 'e': 1