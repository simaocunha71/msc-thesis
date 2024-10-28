```
def fruit_distribution(s, n):
    s = s.split()
    apples = int(s[s.index('apples')-1])
    oranges = int(s[s.index('oranges')-1])
    return n - apples - oranges
```



Explanation:

This function takes two parameters: a string `s` that represents a sentence describing the number of apples and oranges in a basket, and an integer `n` that represents the total number of fruits in the basket.

The function first splits the string `s` into a list of words using the `split()` method. It then finds the indices of the words 'apples' and 'oranges' in the list and subtracts 1 from these indices because the indices are 0-based.

It then converts the words at these indices to integers and subtracts them from `n` to find the number of mango fruits in the basket. The result is returned as the output of the function.

For example, if the input is `fruit_distribution("5 apples and 6 oranges", 19)`, the function will split the string into `['5', 'apples', 'and', '6', 'oranges']`, find the indices of 'apples' and 'oranges', convert them to integers, and subtract them from 19 to get the number of mango fruits, which is 8.

This function works for any sentence that describes the number of apples and oranges in a basket, as long as the sentence follows the same format as the examples provided. It also works for any total number of fruits in the basket, as long as it is a positive integer.