
def sort_third(l: list):
    index = [i for i in range(len(l)) if i % 3 == 0]
    l[:] = [l[i] for i in index if l[i] not in index] + [min(l[i] for i in index if l[i] in index) for _ in index] + [l[i] for i in index if l[i] not in index]
    return l


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("*** Test Passed")
```