Here's a Python function that takes in a string with multiple groups of nested parentheses and returns a list of those groups, separated and balanced:

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are