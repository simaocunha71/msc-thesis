Here is the solution:
```
const checkDictCase = (dict) => {
  if (Object.keys(dict).length === 0) return false;

  const keys = Object.keys(dict);
  const allLower = keys.every((key) => key === key.toLowerCase());
  const allUpper = keys.every((key) => key === key.toUpperCase());

  return allLower || allUpper;
};
```
Explanation:

1. First, we check if the dictionary is empty by checking the length of the keys array. If it's empty, we return false.
2. We get the keys of the dictionary using `Object.keys()`.
3. We use the `every()` method to check if all keys are either all in lower case or all in upper case.
	* `allLower` checks if all keys are equal to their lower case version using `key === key.toLowerCase()`.
	* `allUpper` checks if all keys are equal to their upper case version using `key === key.toUpperCase()`.
4. We return `true` if either `allLower` or `allUpper` is `true`, indicating that all keys are in either lower case or upper case. Otherwise, we return `false`.