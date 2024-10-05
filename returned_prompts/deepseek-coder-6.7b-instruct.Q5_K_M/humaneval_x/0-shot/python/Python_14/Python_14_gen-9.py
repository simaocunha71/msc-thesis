def all_prefixes(string: str) -> List[str]:
    return [string[:i] for i in range(1, len(string) + 1)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

