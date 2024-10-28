from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()
    results = []
    for group in groups:
        count = 0
        max_count = 0
        for char in group:
            if char == '(':
                count += 1
                if count > max_count:
                    max_count = count
            elif char == ')':
                count -= 1
        results.append(max_count)
    return results

print(parse_nested_parens('(()())  ((()))  ()  ((())()())'))

This code works by splitting the input string into groups of parentheses and then for each group, it counts the maximum number of nested parentheses. It does this by incrementing a count each time it encounters an opening parenthesis and decrementing the count each time it encounters a closing parenthesis. The maximum count is stored in max_count. This max_count is appended to the results list for each group and returned at the end.

The time complexity of this code is O(n), where n is the total number of characters in all groups, because it needs to iterate over each character in each group once. The space complexity is O(m), where m is the number of groups, because it creates a new list to store the results.

Please note that this solution assumes that the input string is well-formed and does not contain any invalid characters.
