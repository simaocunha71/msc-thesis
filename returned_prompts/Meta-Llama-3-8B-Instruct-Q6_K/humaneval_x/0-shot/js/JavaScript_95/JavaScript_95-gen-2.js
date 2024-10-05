Here is the solution:

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

This function first checks if the dictionary is empty. If it is, it returns `false`. Then it checks if all keys in the dictionary are in lower case using the `every()` method and the `toLowerCase()` method. It also checks if all keys are in upper case using the `every()` method and the `toUpperCase()` method. If either condition is met, it returns `true`; otherwise, it returns `false`. 

For example, `checkDictCase({"STATE":"NC", "ZIP":"12345" })` returns `true` because all keys are in upper case. `checkDictCase({"a":"apple", "b":"banana"})` returns `true` because all keys are in lower case. `checkDictCase({"a":"apple", "A":"banana", "B":"banana"})` returns `false` because some keys are in upper case and some are in lower case. `checkDictCase({"a":"apple", 8:"banana", "a":"apple"})` returns `false` because the dictionary contains a non-string key (8) and a duplicate key ("a"). `checkDictCase({"Name":"John", "Age":"36", "City":"Houston"})` returns `false` because the dictionary contains keys that are not in all lower case or all upper case. 