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
  let allLower = true;
  let allUpper = true;
  for (const key in dict) {
    if (typeof key !== 'string') return false;
    if (!allLower && !allUpper) return false;
    if (!allLower) allUpper = key === key.toUpperCase();
    if (!allUpper) allLower = key === key.toLowerCase();
  }
  return allLower || allUpper;
}
