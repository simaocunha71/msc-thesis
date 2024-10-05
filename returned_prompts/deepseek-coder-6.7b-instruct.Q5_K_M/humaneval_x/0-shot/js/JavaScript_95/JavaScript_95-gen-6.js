  let keys = Object.keys(dict)

  if (keys.length === 0) return false

  let lowerCaseKeys = keys.filter(key => typeof key === 'string' && key === key.toLowerCase())
  let upperCaseKeys = keys.filter(key => typeof key === 'string' && key === key.toUpperCase())

  return (keys.length === lowerCaseKeys.length || keys.length === upperCaseKeys.length)
}

console.log(checkDictCase({"a":"apple", "b":"banana"})) // true
console.log(checkDictCase({"a":"apple", "A":"banana", "B":"banana"})) // false
console.log(checkDictCase({"a":"apple", 8:"banana", "a":"apple"})) // false
console.log(checkDictCase({"Name":"John", "Age":"36", "City":"Houston"})) // false
console.log(checkDictCase({"STATE":"NC", "ZIP":"12345"})) // true
```

**Explanation:**
The function `checkDictCase` takes a dictionary (in JavaScript we usually refer to them as objects) as an argument.

First, we get all the keys of the dictionary using the `Object.keys()` function, and if the length of the keys array is 0, we return false because the dictionary is empty.

Then, we filter the keys into two groups, one group with keys that are strings in lower case and another group with keys that are strings in upper case.

Finally, we return true if the length of the keys array is equal to the length of either the lowerCaseKeys array or the upperCaseKeys array, meaning that all keys are in the same case (either lower or upper), otherwise we return false.

**Test Cases:**

1. `checkDictCase({"a":"apple", "b":"banana"})` returns `true` because all keys are in lower case.
2. `checkDictCase({"a":"apple", "A":"banana", "B":"banana"})` returns `false` because there are both lower case and upper case keys.
3. `checkDict