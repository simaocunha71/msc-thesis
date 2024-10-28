  if (Object.keys(dict).length === 0) {
    return false;
  }

  let allLower = true;
  let allUpper = true;

  for (const key in dict) {
    if (!allLower) {
      break;
    }
    if (!key.toLowerCase() === key) {
      allLower = false;
    }
  }

  for (const key in dict) {
    if (!allUpper) {
      break;
    }
    if (!key.toUpperCase() === key) {
      allUpper = false;
    }
  }

  return allLower || allUpper;
}
// test cases
console.log(checkDictCase({"a":"apple", "b":"banana"})); // true
console.log(checkDictCase({"a":"apple", "A":"banana", "B":"banana"})); // false
console.log(checkDictCase({"a":"apple", 8:"banana", "a":"apple"})); // false
console.log(checkDictCase({"Name":"John", "Age":"36", "City":"Houston"})); // false
console.log(checkDictCase({"STATE":"NC", "ZIP":"12345" })); // true
console.log(checkDictCase({})); // false
console.log(checkDictCase({"STATE":"NC", "zip":"12345" })); // false
console.log(checkDictCase({"STATE":"NC", "Zip":"12345" })); // true
console.log(checkDictCase({"STATE":"NC", "ziP":"12345" })); // true
console.log(checkDictCase({"STATE":"NC", "zIp":"12345" })); // true
console.log(checkDictCase({"STATE":"NC", "ziPp":"12345" })); // false
console.log(checkDictCase({"STATE":"NC", "ziPp":12345 })); // false
console.log(checkDictCase({"STATE":"NC", 12345:"abc" })); // false
console.log(checkDictCase({"STATE":"NC", "ziP":12345.6 })); // false
console.log(checkDictCase({"STATE":"NC", "ziP":12345.6 })); // false
console.log(checkDictCase({"STATE":"NC", "ziP":12345 })); // false
console.log(checkDictCase({"STATE":"NC", "ziP":12345.0 })); // false
console.log(checkDictCase({"STATE":"NC", "ziP":12345.0 }