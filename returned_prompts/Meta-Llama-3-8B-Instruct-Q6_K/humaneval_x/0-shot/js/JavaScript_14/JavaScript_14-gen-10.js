```
const allPrefixes = (string) => {
  let prefixes = [];
  for (let i = 1; i <= string.length; i++) {
    prefixes.push(string.substring(0, i));
  }
  return prefixes;
};
```


Explanation:
The function `allPrefixes` takes a string as input and returns a list of all prefixes of the string, from shortest to longest.

Here's how it works:

1. Initialize an empty list `prefixes`.
2. Loop through the length of the input string, starting from 1.
3. For each iteration, use the `substring` method to get the prefix of the string from the beginning to the current index `i`.
4. Add the prefix to the `prefixes` list.
5. Return the `prefixes` list.

For example, if the input string is `'abc'`, the function will return the list `['a', 'ab', 'abc']`.