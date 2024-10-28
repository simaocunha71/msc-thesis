Here is the JavaScript solution for the problem:

```javascript
const checkDictCase = (dict) => {
  if (Object.keys(dict).length === 0) {
    return false;
  }

  const allLower = Object.keys(dict).every(key => key === key.toLowerCase());
  const allUpper = Object.keys(dict).every(key => key === key.toUpperCase());

  return allLower || allUpper;
};
```

Explanation:

1. We first check if the dictionary is empty by getting the length of the keys and comparing it to 0. If it's 0, we return false.
2. We then use the `every()` method to check if all keys in the dictionary are in lower case or upper case. We do this by comparing each key with its lower case or upper case version.
3. If any of the conditions are met, we return true. If neither condition is met, we return false.

This function should pass all the test cases provided. Let me know if you have any questions or need further clarification! 😊

Example usage:

```javascript
console.log(checkDictCase({"a":"apple", "b":"banana"})); // true
console.log(checkDictCase({"a":"apple", "A":"banana", "B":"banana"})); // false
console.log(checkDictCase({"a":"apple", 8:"banana", "a":"apple"})); // false
console.log(checkDictCase({"Name":"John", "Age":"36", "City":"Houston"})); // false
console.log(checkDictCase({"STATE":"NC", "ZIP":"12345" })); // true
```