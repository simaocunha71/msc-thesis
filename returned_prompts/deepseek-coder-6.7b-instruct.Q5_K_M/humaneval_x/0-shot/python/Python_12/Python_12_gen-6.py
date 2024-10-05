def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_str = strings[0]
    for string in strings:
        if len(string) > len(longest_str):
            longest_str = string
    return longest_str


print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'



