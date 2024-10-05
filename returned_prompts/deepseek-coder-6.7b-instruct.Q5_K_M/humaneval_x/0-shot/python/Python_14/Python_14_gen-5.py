def all_prefixes(string: str) -> List[str]:
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[0:i])
    return prefixes


print(all_prefixes('abc'))

