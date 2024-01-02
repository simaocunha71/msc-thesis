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
  if (!dict || dict.length === 0) {
    console.log("Given dictionary is empty.");
    return false;
  } else {
    for (var key in dict) {
      let letter = dict[key].toLowerCase();
      if (letter !== dict[key]) {
        return false;
      }
    }
    return true;
  }
};
// https://leetcode.com/problems/check-all-keys-in-a-dictionary-are-in-lowercase-or-uppercase/discuss/365819/C%2B%2B-O(N)