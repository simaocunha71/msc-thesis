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
    if (!Object.keys(dict).length) {
        return true;
     } else {
        let lowerDic = dict;   // making a copy of input dictionary
        for (let key in lowerDic) {
            if (/^[A-Za-z]/.test(key))
                continue;

            if (!/^[A-Za-z0-9]*$/.test(lowerDic[key]) && !/^[A-Za-z0-9.]*$/.test(lowerDic[key])) {
                return false;
            } else {
                continue;
            }
        };
        if (!/^[A-Za-z]/.test(dict["STATE"]) && !/^[A-Za-z0-9.]*$.test(dict["STATE"])) {
            return false;
        } else {
            return true;
     }};
}
module.exports = checkDictCase;