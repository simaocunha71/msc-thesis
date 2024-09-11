```
def number_ctr(s):
    # Use regular expression to count number of digits in a string
    return len(re.findall(r'\d', s))
```

Here's how this solution works:
- We use the `re.findall` method to find all occurrences of a digit in the string.
- The `findall` method returns all occurrences in a list.
- The `len` method is used to get the count of the occurrences.

It's important to note that this code will only count the occurrences of single digits. If you want to count the occurrences of multi-digit numbers, you can use this regex pattern instead: `r'\d+'`.

Here's an example of how you can use this function:
```python
import re

def number_ctr(s):
    return len(re.findall(r'\d', s))

print(number_ctr('program2bedone'))  # Output: 1
```

You can try this function in an interactive Python environment by using the following code:
```python
import re

def number_ctr(s):
    return len(re.findall(r'\d', s))

assert number_ctr('program2bedone') == 1
```

This assertion will pass if the function correctly counts the number of digits in the given string.

Here are some additional resources for further reading:
- [Python Regular Expressions Tutorial](https://docs.python.org/3/library/re.html)
- [How to use Python re.findall()?](https://stackoverflow.com/questions/5962692/how-to-use-python-re-findall)
- [Python re.findall() Not Returning Expected Results](https://stackoverflow.com/questions/17323489/python-re-findall-not-returning-expected-results)

Additionally, if you're interested in learning more about Python testing, you can refer to the following resources:
- [Python unittest — Unit Testing Framework](https://docs.python.org/3/