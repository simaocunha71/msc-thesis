    result = []
    for string in strings:
        if string.startswith(prefix):
            result.append(string)
    return result


# Other solutions:
# from typing import List
# from collections import deque

# def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
#     """ Filter an input list of strings only for ones that start with a given prefix.
#     >>> filter_by_prefix([], 'a')
#     []
#     >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
#     ['abc', 'array']
#     """
#     return [string for string in strings if string.startswith(prefix)]

# def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
#     """ Filter an input list of strings only for ones that start with a given prefix.
#     >>> filter_by_prefix([], 'a')
#     []
#     >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
#     ['abc', 'array']
#     """
#     queue = deque(strings)
#     result = []
#     while queue:
#         item = queue.popleft()
#         if item.startswith(prefix):
#             result.append(item)
#     return result















































































































































































