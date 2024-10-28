

def how_many_times(string: str, substring: str) -> int:
    if len(string) < len(substring):
        return 0
    else:
        return string.count(substring)


# Other solutions:
# def how_many_times(string: str, substring: str) -> int:
#     """ Find how many times a given substring can be found in the original string. Count overlaping cases.
#     >>> how_many_times('', 'a')
#     0
#     >>> how_many_times('aaa', 'a')
#     3
#     >>> how_many_times('aaaa', 'aa')
#     3
#     """
#     return len([1 for i in range(len(string)) if string[i:i + len(substring)] == substring])


# def how_many_times(string: str, substring: str) -> int:
#     return len([1 for i in range(len(string)) if string[i:i + len(substring)] == substring])


# def how_many_times(string: str, substring: str) -> int:
#     return len([x for x in string.split(substring) if x != ''])

# def how_many_times(string: str, substring: str) -> int:
#     return len(string.split(substring)) - 1


```















































































































































































