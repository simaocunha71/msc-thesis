    # your code goes here
    return [i for i in range(len(string) + 1)]


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    # your code goes here
    return [i for i in range(len(string) + 1)]


# Test Cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('ab') == ['a', 'ab']
    assert all_prefixes('a') == ['a']
    print("all tests passed")


test_all_prefixes()





def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    # your code goes here
    return [string[:i] for i in range(len(string) + 1)]


# Test Cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('ab') == ['a', 'ab']
    assert all_prefixes('a') == ['a']
    print("all tests passed")


test_all_prefixes()



def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    # your code goes here
    return [string[:i] for i in range(len(string) + 1)]


# Test Cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('ab') == ['a',