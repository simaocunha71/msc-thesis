```
def extract_rear(tup):
    return [x[-1] for x in tup]
```
This function uses list comprehension to iterate over each string in the tuple and extract the last character using indexing (`x[-1]`). The resulting list of last characters is returned. 

The unit test `assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']` ensures that the function works correctly.  It checks if the output of the function when given the tuple `('Mers', 'for', 'Vers')` is `['s', 'r', 's']`, which is the expected result. 

This function assumes that all strings in the tuple have at least one character, as the problem statement does not specify what should happen if a string is empty. If empty strings are a possibility, you might want to add some error checking code to handle this case.  For example, you could filter out empty strings before processing the remaining strings: `return [x[-1] for x in tup if x]`.  However, this is not necessary based on the provided unit test. 