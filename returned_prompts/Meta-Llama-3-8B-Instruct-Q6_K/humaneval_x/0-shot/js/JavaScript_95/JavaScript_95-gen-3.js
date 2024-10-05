Here is a JavaScript function that fulfills the requirement:

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

This function first checks if the dictionary is empty by checking the length of the keys. If the dictionary is empty, it returns false. Then it checks if all keys are in lower case or all keys are in upper case by using the `every` method and comparing each key with its lower case or upper case version. If any of these conditions are met, it returns true. Otherwise, it returns false.