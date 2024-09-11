def extract_quotation(s):
    l = []
    while True:
        if s.find('"') == 0:
            break
        i = s.find('"')
        j = s.find('"', i + 1)
        l.append(s[i + 1 : j])
        s = s[j:]
    return l


# assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']


def extract_quotation(s):
    l = []
    while True:
        if s.find('"') == 0:
            break
        i = s.find('"')
        j = s.find('"', i + 1)
        l.append(s[i + 1 : j])
        s = s[j:]
    return l


# assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']


"""
Write a function that returns the index of the first character of the longest word in a string.

assert find_longest_word(s) == 7
"""

def find_longest_word(s):
    l = s.split()
    longest = max(l, key=len)
    i = s.index(longest)
    return i


# assert find_longest_word('The quick brown fox jumped over the lazy dog') == 7


"""
Write a function that takes a list of strings and returns a list of strings with the first letter of each word capitalized.

assert capitalize_list(['the', 'quick', 'brown', 'fox']) == ['The', 'Quick', 'Brown', 'Fox']
"""

def capitalize_list(l):
    return [word.capitalize() for word in l]


# assert capitalize_list(['the', 'quick', 'brown', 'fox']) == ['The', 'Quick', 'Brown', 'Fox']

"""
Write a function that returns the first n