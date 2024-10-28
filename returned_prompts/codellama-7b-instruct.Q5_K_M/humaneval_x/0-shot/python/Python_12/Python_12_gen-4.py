def longest(strings: List[str]) -> Optional[str]:
    longest = None
    for s in strings:
        if len(s) > len(longest) or (len(s) == len(longest) and longest is None):
            longest = s
    return longest
