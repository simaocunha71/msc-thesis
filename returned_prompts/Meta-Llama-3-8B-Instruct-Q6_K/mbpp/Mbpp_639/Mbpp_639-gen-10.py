```
def sample_nam(nam):
    return sum(len(name) for name in nam if name[0].isupper())
```



This function uses a generator expression to iterate over the list of names. It checks if the first character of each name is uppercase using the `isupper()` method. If it is, it adds the length of the name to the sum. The `sum()` function then adds up these lengths to give the total. 

For example, if the input is `['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']`, the function will return `16`, because 'Dylan', 'Diana', and 'Joanne' are the only names that start with an uppercase letter, and their lengths are 5, 6, and 7, respectively. 

The unit test `assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16` confirms this. 





Final Answer: The final answer is def sample_nam(nam): return sum(len(name) for name in nam if name[0].isupper()). I hope it is correct.