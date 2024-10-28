

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    while string != "":
        pos = string.find(substring)
        if pos != -1:
            count += 1
            string = string[pos + 1:]
        else:
            break
    return count


# Other Solutions:
# Pythonic solution:
# from collections import defaultdict
# def how_many_times(string: str, substring: str) -> int:
#     """ Find how many times a given substring can be found in the original string. Count overlaping cases.
#     >>> how_many_times('', 'a')
#     0
#     >>> how_many_times('aaa', 'a')
#     3
#     >>> how_many_times('aaaa', 'aa')
#     3
#     """
#     return len(string) - len(string.replace(substring, '')) // len(substring)

# Recursive solution:
# def how_many_times(string: str, substring: str) -> int:
#     """ Find how many times a given substring can be found in the original string. Count overlaping cases.
#     >>> how_many_times('', 'a')
#     0
#     >>> how_many_times('aaa', 'a')
#     3
#     >>> how_many_times('aaaa', 'aa')
#     3
#     """
#     if len(string) == 0:
#         return 0
#     elif string[:len(substring)] == substring:
#         return 1 + how_many_times(string[len(substring):], substring)
#     else:
#         return how_many_times(string[1:], substring)







``