Here's the solution that generates all prefixes from shortest to longest of the input string:

```javascript
const allPrefixes = (string) => {
  let prefixes = [];
  for (let i = 0; i < string.length; i++) {
    prefixes.push(string.slice(0, i + 1));
  }
  return prefixes;
};
```

In this code, we create an empty array `prefixes` to store all the prefixes. Then, we use a `for` loop to iterate over the input string. In each iteration, we use the `slice()` method to get a prefix of the string from the start up to the current index `i + 1`. We then push this prefix into the `prefixes` array. Finally, we return the `prefixes` array.