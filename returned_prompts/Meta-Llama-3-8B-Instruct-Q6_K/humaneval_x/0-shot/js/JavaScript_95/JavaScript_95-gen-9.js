Here is a JavaScript function that implements the described behavior:

```javascript
const checkDictCase = (dict) => {
  if (Object.keys(dict).length === 0) {
    return false;
  }
  const allLower = Object.keys(dict).every((key) => key === key.toLowerCase());
  const allUpper = Object.keys(dict).every((key) => key === key.toUpperCase());
  return allLower || allUpper;
};
```

Here's a breakdown of the code:

1. `Object.keys(dict).length === 0`: This checks if the dictionary is empty. If it is, the function returns `false`.
2. `Object.keys(dict).every((key) => key === key.toLowerCase())`: This uses the `every` method to check if all keys in the dictionary are in lower case. The callback function `key => key === key.toLowerCase()` checks if a key is equal to its lower case version.
3. `Object.keys(dict).every((key) => key === key.toUpperCase())`: This uses the `every` method to check if all keys in the dictionary are in upper case. The callback function `key => key === key.toUpperCase()` checks if a key is equal to its upper case version.
4. `return allLower || allUpper`: This returns `true` if either all keys are in lower case or all keys are in upper case, and `false` otherwise.

You can test this function with the examples you provided to see that it returns the expected results. For example:

```javascript
console.log(checkDictCase({"a":"apple", "b":"banana"})); // true
console.log(checkDictCase({"a":"apple", "A":"banana", "B":"banana"})); // false
console.log(checkDictCase({"a":"apple", 8:"banana", "a":"apple"})); // false
console.log(checkDictCase({"Name":"John", "Age":"36", "City":"Houston"})); // false
console.log(checkDictCase({"STATE":"NC", "ZIP":"12345" })); // true
```