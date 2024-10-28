Here is a JavaScript solution for the problem:

```javascript
const checkDictCase = (dict) => {
  if (Object.keys(dict).length === 0) return false;
  let allLower = true;
  let allUpper = true;
  for (let key in dict) {
    if (!key.match(/^([a-z]+)$/)) {
      allLower = false;
    }
    if (!key.match(/^([A-Z]+)$/)) {
      allUpper = false;
    }
  }
  return allLower || allUpper;
};
```

This function works by first checking if the dictionary is empty. If it is, the function immediately returns `false`. Then, it initializes two variables, `allLower` and `allUpper`, to `true`. These variables will be used to track whether all keys in the dictionary are in lower case or upper case.

The function then iterates over each key in the dictionary. For each key, it checks if the key matches the pattern for a string in lower case or upper case using regular expressions. If a key does not match either pattern, the corresponding variable (`allLower` or `allUpper`) is set to `false`.

Finally, the function returns `true` if either `allLower` or `allUpper` is `true`, indicating that all keys in the dictionary are in the same case. Otherwise, it returns `false`.