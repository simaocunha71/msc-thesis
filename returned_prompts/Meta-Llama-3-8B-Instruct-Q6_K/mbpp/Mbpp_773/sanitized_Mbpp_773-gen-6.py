from collections import defaultdict
def occurance_substring(string: str, substring: str) -> tuple:
    if substring not in string:
        return None
    occurrences = defaultdict(list)
    start = 0
    while start < len(string):
        start = string.find(substring, start)
        if start == -1:
            break
        occurrences[len(occurrences)].append(start)
        start += 1
    return (substring, occurrences[0][0], occurrences[0][0] + len(substring) - 1) if occurrences else None