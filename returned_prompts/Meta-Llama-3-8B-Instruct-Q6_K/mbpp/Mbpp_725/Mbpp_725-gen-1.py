You can use the re module in Python to extract values between quotation marks. Here's how you can do it:
```
import re

def extract_quotation(s):
    return re.findall(r'"([^"]*)"', s)
```
This function uses a regular expression to find all occurrences of a string enclosed in quotation marks. The regular expression r'"([^"]*)"' matches a string that starts with a double quote, followed by any characters (captured in a group), and ends with a double quote. The re.findall function returns all non-overlapping matches of this regular expression in the string as a list of strings. 

For example, if you call `extract_quotation('Cortex "A53" Based "multi" tasking "Processor"')`, it will return `['A53', 'multi', 'Processor']`. 
```
print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))
```



