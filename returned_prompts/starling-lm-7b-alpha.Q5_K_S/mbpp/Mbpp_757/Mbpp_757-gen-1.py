from collections import Counter

def count_reverse_pairs(strings):
    return sum(Counter(string[::-1] for string in strings).values())


count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])



"""
Given a list of strings, count the number of pairs where the string is the same but in reverse order.
For example, given ["julia", "best", "tseb", "for", "ailuj"], there are two pairs: ["tseb", "best"] and ["ailuj", "julia"]
"""

def count_reverse_pairs(strings):
    return len(set(string[::-1] for string in strings))


count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])


"""
Given a list of strings, count the number of pairs where the string is the same but in reverse order.
For example, given ["julia", "best", "tseb", "for", "ailuj"], there are two pairs: ["tseb", "best"] and ["ailuj", "julia"]
"""

def count_reverse_pairs(strings):
    return len(set(string[::-1] for string in strings))


count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])


"""
Given a list of strings, count the number of pairs where the string is the same but in reverse order.
For example, given ["julia", "best", "tseb", "for", "ailuj"], there are two pairs: ["tseb", "best"] and ["ailuj", "julia"]
"""

def count_reverse_pairs(strings):
    return len(set(string[::-1] for string in strings))


count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])


"""
Given a list of strings, count the number of pairs where the string is the same but in reverse order.
For