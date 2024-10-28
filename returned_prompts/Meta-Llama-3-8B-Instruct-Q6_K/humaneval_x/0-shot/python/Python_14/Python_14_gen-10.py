from typing import List

def all_prefixes(string: str) -> List[str]:
    result = []
    for i in range(1, len(string) + 1):
        result.append(string[:i])
    return result

print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
print(all_prefixes('a'))  # Output: ['a']
print(all_prefixes(''))  # Output: []


# Test cases
assert all_prefixes('abc') == ['a', 'ab', 'abc'], f"Expected all_prefixes('abc') to return ['a', 'ab', 'abc'], but got {all_prefixes('abc')}"
assert all_prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hello'], f"Expected all_prefixes('hello') to return ['h', 'he', 'hel', 'hell', 'hello'], but got {all_prefixes('hello')}"
assert all_prefixes('a') == ['a'], f"Expected all_prefixes('a') to return ['a'], but got {all_prefixes('a')}"
assert all_prefixes('') == [], f"Expected all_prefixes('') to return [], but got {all_prefixes('')}"
print("All test cases pass!")  # If the test cases don't fail, then all test cases pass!  # Output: All test cases pass!  # This means the function all_prefixes() is working correctly.  # Note: The function all_prefixes() will return an empty list for an empty string.  # This is because there are no prefixes for an empty string.  # The function works correctly for strings of all lengths.  # It returns a list of all prefixes of the input string, from shortest to longest.  # It can be used to solve problems that involve processing all prefixes of a string.  # The function is efficient because it uses a simple loop and does not use any advanced data structures.  # It can be used in a variety of applications, such as text processing, string manipulation, and data analysis.  # The function is easy to understand and use, and it can be used by developers of all skill levels.  # It is a useful tool for any developer who needs to process all prefixes of a string.  # The