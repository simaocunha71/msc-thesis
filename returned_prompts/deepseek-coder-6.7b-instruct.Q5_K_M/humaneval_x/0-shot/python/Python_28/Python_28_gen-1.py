def concatenate(strings: List[str]) -> str:
    return "".join(strings)


print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'


# You can also do this in a more Pythonic way using the `join()` method:
# def concatenate(strings: List[str]) -> str:
#     return "".join(strings)

# print(concatenate([]))  # ''
# print(concatenate(['a', 'b', 'c']))  # 'abc'


# Or using a loop:
# def concatenate(strings: List[str]) -> str:
#     result = ""
#     for s in strings:
#         result += s
#     return result

# print(concatenate([]))  # ''
# print(concatenate(['a', 'b', 'c']))  # 'abc'


# Or using a list comprehension:
# def concatenate(strings: List[str]) -> str:
#     return "".join([s for s in strings])

# print(concatenate([]))  # ''
# print(concatenate(['a', 'b', 'c']))  # 'abc'


# Or using a recursive function:
# def concatenate(strings: List[str]) -> str:
#     if len(strings) == 0:
#         return ""
#     else:
#         return strings[0] + concatenate(strings[1:])

# print(concatenate([]))  # ''
# print(concatenate(['a', 'b', 'c']))  # 'abc'


# Or using a one-liner using the `reduce()` function:
# from functools import reduce
# def concatenate(strings: List[str]) -> str:
#     return reduce(lambda a, b: a + b, strings)

# print(concatenate([]))  # ''
# print(concatenate(['a', 'b', 'c']))  # 'abc'


# Or using a generator