Here is the Python function for the problem:

```python
import re

def extract_quotation(s):
    return re.findall(r'"([^"]*)"', s)
```

In this function, we use regular expression to find all the strings enclosed in quotation marks. The regular expression pattern `r'"([^"]*)"'` is used to match the quotation marks and the content inside them. The content inside quotations is captured inside the parentheses `()` which forms a group. The `[^"]*` part of the pattern matches any character that is not a quotation mark, zero or more times. The whole pattern is enclosed in quotation marks `"` to treat it as a string.

You can test the function with the provided test case:

```python
print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"')) 
# Output: ['A53', 'multi', 'Processor']
```

This output matches the expected result.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
