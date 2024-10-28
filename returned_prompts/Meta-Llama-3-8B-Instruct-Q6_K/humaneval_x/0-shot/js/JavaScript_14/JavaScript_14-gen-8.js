```
const allPrefixes = (string) => {
  const result = [];
  for (let i = 1; i <= string.length; i++) {
    result.push(string.substring(0, i));
  }
  return result;
};
```



Explanation:
The function `allPrefixes` takes a string as input and returns a list of all its prefixes from shortest to longest.

The function uses a `for` loop to iterate over the length of the input string. For each iteration, it uses the `substring` method to extract the prefix of the string from the beginning up to the current index `i`. This prefix is then pushed onto the `result` array.

The function returns the `result` array, which contains all the prefixes of the input string in the order of shortest to longest.

For example, if the input string is `'abc'`, the function will return the list `['a', 'ab', 'abc']`, which are all the prefixes of the string in the order of shortest to longest.