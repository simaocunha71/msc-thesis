To solve this problem, we need to check the case of each key in the dictionary. If all keys are lowercase or all keys are uppercase, we return true. Otherwise, we return false. 

Here is the implementation:
```javascript
const checkDictCase = (dict) => {
  // Check if the dictionary is empty
  if (Object.keys(dict).length === 0) {
    return false;
  }

  // Get the case of the first key
  const firstKey = Object.keys(dict)[0];
  const firstKeyIsLowerCase = firstKey === firstKey.toLowerCase();
  const firstKeyIsUpperCase = firstKey === firstKey.toUpperCase();

  // Check the case of all keys
  for (const key in dict) {
    if ((firstKeyIsLowerCase && key !== key.toLowerCase()) || (firstKeyIsUpperCase && key !== key.toUpperCase())) {
      return false;
    }
  }

  return true;
};
```

We can test the function with the provided examples:
```javascript
console.log(checkDictCase({"a":"apple", "b":"banana"})); // true
console.log(checkDictCase({"a":"apple", "A":"banana", "B":"banana"})); // false
console.log(checkDictCase({"a":"apple", 8:"banana", "a":"apple"})); // false
console.log(checkDictCase({"Name":"John", "Age":"36", "City":"Houston"})); // false
console.log(checkDictCase({"STATE":"NC", "ZIP":"12345" })); // true
```