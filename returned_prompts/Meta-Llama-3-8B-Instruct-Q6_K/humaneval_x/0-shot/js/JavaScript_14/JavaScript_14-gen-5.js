```
const allPrefixes = (string) => {
  let result = [];
  for(let i = 1; i <= string.length; i++) {
    result.push(string.substring(0, i));
  }
  return result;
};
```


This function uses a for loop to generate all prefixes of the input string. The `substring(0, i)` method returns a new string containing the characters from the beginning of the string to the `i`-th character. The `push` method adds each prefix to the `result` array. The function then returns the `result` array, which contains all prefixes of the input string, from shortest to longest.