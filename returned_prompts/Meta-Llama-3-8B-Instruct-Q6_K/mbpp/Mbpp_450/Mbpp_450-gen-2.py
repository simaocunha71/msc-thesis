```
def extract_string(lst, size):
    return [i for i in lst if len(i) == size]
```


The function `extract_string` takes two parameters: `lst` (a list of strings) and `size` (an integer). It returns a new list containing only the strings from `lst` that have a length equal to `size`. The function uses a list comprehension to iterate over the strings in `lst`, checks if the length of each string is equal to `size`, and adds the string to the new list if it is.

For example, if we call `extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)`, the function will return `['practice', 'solution']`, because these are the only strings in the list that have a length of 8. The other strings have lengths of 6, 4, 10, and 7, so they are not included in the result. The function will return an empty list if there are no strings in the input list with the specified length. 







