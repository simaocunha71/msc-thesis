```javascript
const checkDictCase = (dict) => {
  // Check if dictionary is empty
  if (Object.keys(dict).length === 0) return false;

  // Check if all keys are strings
  for (let key in dict) {
    if (typeof key !== 'string') return false;
  }

  // Check if all keys are in lower case or upper case
  const areLower = Object.keys(dict).every(key => key === key.toLowerCase());
  const areUpper = Object.keys(dict).every(key => key === key.toUpperCase());

  return areLower || areUpper;
};
```

This function first checks if the dictionary is empty and returns false if it is. Then it checks if all keys are strings. If any key is not a string, it returns false. Finally, it checks if all keys are in lower case or upper case using the `every` method and returns the result.