You can solve this problem by using regular expression. The regular expression pattern '\\"[^"]+"|"[^"]+"|\'[^"]+\'' will match any string enclosed in either double quotes or single quotes. 

Here is the Python function:

```
import re
def extract_quotation(s):
    return re.findall(r'\"[^"]+\"|\'[^"]+\'', s)
```

This function uses the `findall` function of the `re` module to find all occurrences of the given pattern in the string. The pattern is a regular expression that matches either a string enclosed in double quotes or a string enclosed in single quotes. The `[^"]+` part of the pattern matches any characters that are not a double quote, and the `+` after it means that it should match one or more of these characters. The `\"` and `\'` are used to match the double quotes and single quotes, respectively.

For example, if you call `extract_quotation('Cortex "A53" Based "multi" tasking "Processor"')`, the function will return `['"A53"', '"multi"', '"Processor"']`, which are the strings enclosed in double quotes. If you want to get the strings without the quotes, you can use a list comprehension to remove the quotes:

```
def extract_quotation(s):
    return [x.strip('"').strip("'") for x in re.findall(r'\"[^"]+\"|\'[^"]+\'', s)]
```

This function will return `['A53', 'multi', 'Processor']`, which are the strings enclosed in double quotes and single quotes without the quotes.  This function works for strings enclosed in both double quotes and single quotes, and it returns the strings without the quotes.  It also works for strings that are enclosed in both double quotes and single quotes, and it returns the strings without the quotes.  For example, if you call `extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'), it will return `['A53', 'multi', 'Processor']`.  If you call `extract_quotation("Cortex 'A53' Based 'multi' tasking 'Processor'"), it will also return `['A53', 'multi', 'Processor']`.  If you call `extract_quotation("Cortex 'A53' Based 'multi' tasking 'Processor'"), it will return `['A53', 'multi',