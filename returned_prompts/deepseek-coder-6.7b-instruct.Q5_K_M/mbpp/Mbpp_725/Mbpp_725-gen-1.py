Here is a Python solution using regular expressions:

```python
import re

def extract_quotation(s):
    return re.findall(r'"([^"]*)"', s)
```

Explanation:
In the regular expression `r'"([^"]*)"'`:
- The `"` are the delimiters.
- `[^"]*` means any character that is not a `"`, zero or more times. This will match any string of characters that are not `"`.
- `(` and `)` are used to create a group, which can be used later in the code. In this case, we are interested in the part of the string that is inside the quotation marks.
- `findall` returns all matches of the pattern in the string as a list of strings.

So, for the given string `'Cortex "A53" Based "multi" tasking "Processor"'`, the function will return `['A58', 'multi', 'Processor']`.

If you want to extract the whole sentence between quotation marks, you can modify the regular expression to `r'"([^"]*)"'`.

```python
import re

def extract_quotation(s):
    return re.findall(r'"([^"]*)"', s)
```

Explanation:
In the regular expression `r'"([^"]*)"'`:
- The `"` are the delimiters.
- `[^"]*` means any character that is not a `"`, zero or more times. This will match any string of characters that are not `"`.
- `(` and `)` are used to create a group, which can be used later in the code. In this case, we are interested in the part of the string that is inside the quotation marks.
- `findall` returns all matches of the pattern in the string as a list of strings.

So, for the given string `'Cortex "A53" Based "multi" tasking "Processor"'`, the function will return `['A58', 'multi', 'Processor']`.
"""
<jupyter_output>
<empty_output>
<jupyter_