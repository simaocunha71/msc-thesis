Here is a JavaScript solution for the problem:

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

This function first checks if the dictionary is empty. If it is, it returns false. Then it checks if all keys are in lower case or all keys are in upper case using the every() method. The every() method returns true if every element in the array (or in this case, every key in the dictionary) passes the test implemented by the provided function. If all keys are in lower case or all keys are in upper case, the function returns true, otherwise it returns false.