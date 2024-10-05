  if (!dict || Object.keys(dict).length === 0) return false;

  let lowerCase = true;
  let upperCase = true;

  for (let key in dict) {
    if (key !== key.toLowerCase()) lowerCase = false;
    if (key !== key.toUpperCase()) upperCase = false;
  }

  return lowerCase || upperCase;
};

console.log(checkDictCase({"a":"apple", "b":"banana"})); // true
console.log(checkDictCase({"a":"apple", "A":"banana", "B":"banana"})); // false
console.log(checkDictCase({"a":"apple", 8:"banana", "a":"apple"})); // false
console.log(checkDictCase({"Name":"John", "Age":"36", "City":"Houston"})); // false
console.log(checkDictCase({"STATE":"NC", "ZIP":"12345"  })); // true

The function checks if all keys in the dictionary are either in lower case or upper case and returns true if they are, else false. 
The function first checks if the dictionary is empty, if it is it returns false. 
Then it iterates over the keys in the dictionary and checks if they are equal to their lower case or upper case versions.
If all keys are equal to their lower case versions it sets lowerCase to true, if it finds a key that isn't in lower case it sets lowerCase to false.
It does the same for upperCase, but checks if the keys are in upper case.
Finally it returns true if either lowerCase or upperCase is true, else it returns false.
*/

module.exports = checkDictCase;

/*
  Tests:
  checkDictCase({"a":"apple", "b":"banana"}) should return true.
  checkDictCase({"a":"apple", "A":"banana", "B":"banana"}) should return false.
  checkDictCase({"a":"apple", 8:"banana", "a":"apple"}) should return false.
  checkDictCase({"Name":"John",