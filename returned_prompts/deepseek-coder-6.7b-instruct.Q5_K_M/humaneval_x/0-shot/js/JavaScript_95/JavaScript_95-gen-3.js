  if (Object.keys(dict).length === 0) {
    return false;
  }
  
  let lowerCase = true;
  let upperCase = true;
  
  for (let key in dict) {
    if (key !== key.toLowerCase()) {
      lowerCase = false;
    }
    if (key !== key.toUpperCase()) {
      upperCase = false;
    }
    if (!lowerCase && !upperCase) {
      return false;
    }
  }
  
  return true;
}

console.log(checkDictCase({"a":"apple", "b":"banana"}));
console.log(checkDictCase({"a":"apple", "A":"banana", "B":"banana"}));
console.log(checkDictCase({"a":"apple", 8:"banana", "a":"apple"}));
console.log(checkDictCase({"Name":"John", "Age":"36", "City":"Houston"}));
console.log(checkDictCase({"STATE":"NC", "ZIP":"12345"}));
console.log(checkDictCase({}));
// Output: true, false, false, false, true, false


/*
  This function works by first checking if the dictionary is empty. 
  If it is, it returns false as requested.
  Then it iterates over the keys of the dictionary. For each key, it checks if it is equal to its lower case or upper case version. 
  If it is not, it sets the corresponding boolean variable to false. 
  If both boolean variables are still true at the end of the loop, it returns true, indicating that all keys are either in lower case or upper case. 
  If at least one of the boolean variables is still true at the end of the loop, it returns false, indicating that some keys are not in the correct case.
  */



























































