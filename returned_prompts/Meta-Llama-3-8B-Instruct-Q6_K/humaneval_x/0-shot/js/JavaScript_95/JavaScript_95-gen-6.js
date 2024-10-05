```
function checkDictCase(dict) {
  if (Object.keys(dict).length === 0) return false;

  const allLower = Object.keys(dict).every(key => key === key.toLowerCase());
  const allUpper = Object.keys(dict).every(key => key === key.toUpperCase());

  return allLower || allUpper;
}
```


Explanation:

1. We first check if the dictionary is empty by checking the length of the keys. If it is empty, we return `false`.

2. We then use the `every()` method to check if all keys in the dictionary are either in lower case or in upper case.

3. We use the `toLowerCase()` and `toUpperCase()` methods to convert the key to lower case and upper case respectively.

4. We use the logical OR operator (`||`) to return `true` if either `allLower` or `allUpper` is `true`, indicating that all keys are in either lower case or upper case. If neither is `true`, the function returns `false`.

5. This function will return `true` if all keys are in lower case, all keys are in upper case, or if the dictionary is empty. Otherwise, it will return `false`.