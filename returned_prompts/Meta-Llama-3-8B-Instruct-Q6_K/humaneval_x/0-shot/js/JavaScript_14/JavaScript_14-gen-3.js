```
  return [...string].reduce((acc, char, i) => {
    acc.push(string.slice(0, i + 1));
    return acc;
  }, []);
```


Explanation:
The function `allPrefixes` takes a string as an argument and returns an array of all prefixes of the string from shortest to longest.

The function uses the `reduce` method to iterate over the characters in the string. For each character, it adds the substring from the beginning of the string to the current character to the accumulator array `acc`.

The `acc` array is initialized as an empty array `[]`. The `reduce` method is called with the initial value `[]` and a callback function that takes three arguments: the accumulator array `acc`, the current character `char`, and the current index `i`.

In the callback function, `acc.push(string.slice(0, i + 1))` adds the substring from the beginning of the string to the current character to the accumulator array `acc`.

Finally, the `reduce` method returns the accumulator array `acc`, which contains all prefixes of the input string from shortest to longest.

For example, if the input string is `'abc'`, the function will return the array `['a', 'ab', 'abc']`, which are all prefixes of the string in order from shortest to longest.