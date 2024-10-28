/*
  Given a dictionary, return true if all keys are strings in lower 
  case or all keys are strings in upper case, else return false.
  The function should return false is the given dictionary is empty.
  Examples:
  checkDictCase({"a":"apple", "b":"banana"}) should return true.
  checkDictCase({"a":"apple", "A":"banana", "B":"banana"}) should return false.
  checkDictCase({"a":"apple", 8:"banana", "a":"apple"}) should return false.
  checkDictCase({"Name":"John", "Age":"36", "City":"Houston"}) should return false.
  checkDictCase({"STATE":"NC", "ZIP":"12345" }) should return true.
  */
const checkDictCase = (dict) => {

  if (Object.keys(dict).length === 0) return false;

  let isAllLower = true;
  let isAllUpper = true;

  for (let key in dict) {
    if (!isAllLower) break;
    isAllLower = (key === key.toLowerCase());
  }

  for (let key in dict) {
    if (!isAllUpper) break;
    isAllUpper = (key === key.toUpperCase());
  }

  return (isAllLower || isAllUpper);
}

