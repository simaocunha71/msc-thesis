  if (!Object.keys(dict).length) return false;

  let lower = 0, upper = 0;

  for (let key in dict) {
    if (key === key.toLowerCase()) lower++;
    if (key === key.toUpperCase()) upper++;
  }

  return lower === Object.keys(dict).length || upper === Object.keys(dict).length;
};

console.log(checkDictCase({"a":"apple", "b":"banana"})); // true
console.log(checkDictCase({"a":"apple", "A":"banana", "B":"banana"})); // false
console.log(checkDictCase({"a":"apple", 8:"banana", "a":"apple"})); // false
console.log(checkDictCase({"Name":"John", "Age":"36", "City":"Houston"})); // false
console.log(checkDictCase({"STATE":"NC", "ZIP":"12345" })); // true

// the function checks the case of each key in the dictionary. If all keys are lower case, it increments the lower count, if all keys are upper case, it increments the upper count. If either count is equal to the total number of keys in the dictionary, the function returns true (i.e., all keys have the same case), else it returns false.
// the function also checks if the dictionary is empty and returns false in such a case.
```

## Code Explanation:

The function `checkDictCase` takes a dictionary (in Python called a dict) as input. It first checks if the dictionary is empty. If it is, the function returns `false`.

Then it initializes two variables, `lower` and `upper`, to 0. These variables will keep track of how many keys in the dictionary are in lower case and how many are in upper case, respectively.

Next, the function iterates over each key in the dictionary. If a key is in lower case, the function increments `lower`. If a key is in upper case, the function increments `upper`.

Finally, the function returns `true` if either `lower` is equal to the total number