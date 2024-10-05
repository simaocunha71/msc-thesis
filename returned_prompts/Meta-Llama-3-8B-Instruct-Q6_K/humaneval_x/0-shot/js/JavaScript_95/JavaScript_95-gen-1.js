```
const checkDictCase = (dict) => {
  if (Object.keys(dict).length === 0) return false;
  const allLower = Object.keys(dict).every(key => key.toLowerCase() === key);
  const allUpper = Object.keys(dict).every(key => key.toUpperCase() === key);
  return allLower || allUpper;
};
```
Explanation:
The function `checkDictCase` takes a dictionary `dict` as an argument. It first checks if the dictionary is empty using `Object.keys(dict).length === 0`. If it is, the function returns `false`.

Then, it uses the `every` method to check if all keys in the dictionary are either in lower case or in upper case. The `every` method returns `true` if all elements in the array (in this case, the keys of the dictionary) pass the test implemented by the provided function.

The `every` method is called twice: once with a function that checks if a key is in lower case (`key.toLowerCase() === key`), and once with a function that checks if a key is in upper case (`key.toUpperCase() === key`). The `||` operator is used to return `true` if either condition is met.

If the dictionary is not empty and all keys are either in lower case or in upper case, the function returns `true`. Otherwise, it returns `false`.