```
def fix_spaces(text):
    text = text.replace(" ", "_")
    return text.replace("  ", "-")
```


Explanation:
The function takes a string `text` as input and returns a new string with all spaces replaced with underscores and consecutive spaces replaced with hyphens.

1. `text.replace(" ", "_")` replaces all spaces with underscores.
2. `text.replace("  ", "-")` replaces all consecutive spaces with hyphens. This is done after replacing all individual spaces with underscores to ensure that consecutive spaces are correctly replaced with hyphens.

For example, if the input is `"Example   3"`, the function will first replace all individual spaces with underscores, resulting in `"Example_   3"`, and then replace all consecutive spaces with hyphens, resulting in `_Example-3`. 





