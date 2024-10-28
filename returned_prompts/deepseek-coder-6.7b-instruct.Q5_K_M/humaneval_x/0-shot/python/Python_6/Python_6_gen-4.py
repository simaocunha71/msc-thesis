```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()
    results = []
    for group in groups:
        count = 0
        max_count = 0
        for char in group:
            if char == "(":
                count += 1
                if count > max_count:
                    max_count = count
            elif char == ")":
                count -= 1
        results.append(max_count)
    return results


print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

Output:

```python
[2, 3, 1, 3]
```

Explanation:

In the function `parse_nested_parens()`, we first split the input string into a list of groups, each group being separated by a space.

Next, we initialize an empty list `results` to store the maximum depth of nesting for each group.

We then iterate over each group in the list of groups. For each group, we initialize a `count` variable to 0 and a `max_count` variable to 0. These variables will keep track of the current level of nesting and the maximum level of nesting found so far, respectively.

We then iterate over each character in the group. If the character is an opening parenthesis `(`, we increment the `count` and if `count` is greater than `max_count`, we update `max_count`. If the character is a closing parenthesis `)`, we decrement the `count`.

After iterating over all characters in the group, we append `max_count` to the `results` list.

Finally, we return the `results` list.

For the input '(()()) ((())) () ((())()())', the function returns [2, 3, 1, 3] as expected.
"""
```

## Code:

```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()
    results