    result = []
    for string in strings:
        if substring in string:
            result.append(string)
    return result


# These "asserts" using only for self-checking and not necessary
# for auto-testing

assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']


# Some extra credit tests

assert filter_by_substring(['python', 'C', 'ruby', 'go', 'kotlin'], 'py') == ['python']
assert filter_by_substring(['apple', 'apricot', 'cherry', 'kiwi'], 'p') == ['apple', 'apricot']
assert filter_by_substring(['banana', 'blueberry'], 'berry') == ['blueberry']
assert filter_by_substring(['apple', 'banana', 'pear'], 'pe') == ['pear']


# Some extra credit tests with empty substring

assert filter_by_substring(['python', 'C', 'ruby', 'go', 'kotlin'], '') == []
assert filter_by_substring(['apple', 'apricot', 'cherry', 'kiwi'], '') == ['apple', 'apricot', 'cherry', 'kiwi']


# Some edge cases

assert filter_by_substring([], 'z') == []
assert filter_by_substring(['abc'], 'b') == ['abc']





























































































































































