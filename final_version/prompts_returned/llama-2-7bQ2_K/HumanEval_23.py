

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string.lstrip())

if __name__ == "__main__":
    inp = input()
    print(' '.join([str(out) for out in [str(item) for item in map(str, [int(i), strlen(inp), i]) if (i < 6 or len(str(int(i))) == 1)]]))