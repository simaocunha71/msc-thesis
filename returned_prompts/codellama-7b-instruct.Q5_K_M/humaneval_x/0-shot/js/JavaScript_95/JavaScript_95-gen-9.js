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
  if(!dict) return false;
  const keys = Object.keys(dict);
  if(keys.length === 0) return false;
  const lowerCase = keys.every(key => key.toLowerCase() === key);
  const upperCase = keys.every(key => key.toUpperCase() === key);
  return lowerCase || upperCase;
}
