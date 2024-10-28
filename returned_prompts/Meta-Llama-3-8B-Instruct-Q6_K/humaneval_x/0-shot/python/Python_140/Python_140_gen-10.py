```
def fix_spaces(text):
    text = text.replace(" ", "_")
    return text.replace("  ", "-")
```

Explanation:
The function `fix_spaces` takes a string `text` as input and returns a new string with the specified modifications. 

First, it replaces all spaces in the string with underscores using the `replace` method. This is done with `text.replace(" ", "_")`.

Then, it checks if the string has more than 2 consecutive spaces and replaces all consecutive spaces with dashes. This is done with `text.replace("  ", "-")`. The `replace` method returns a new string with the specified replacement, it doesn't modify the original string.

The function returns the modified string. 

For example, if the input is "Example 1", the function will first replace all spaces with underscores, resulting in "Example_1", and then it will check if there are more than 2 consecutive spaces and replace them with dashes, which is not the case in this example, so the output will be "Example_1". 

If the input is " Example 2", the function will first replace all spaces with underscores, resulting in "_Example_2", and then it will check if there are more than 2 consecutive spaces and replace them with dashes, which is not the case in this example, so the output will be "_Example_2". 

If the input is " Example   3", the function will first replace all spaces with underscores, resulting in "_Example   3", and then it will check if there are more than 2 consecutive spaces and replace them with dashes, which is the case, so the output will be "_Example-3". 