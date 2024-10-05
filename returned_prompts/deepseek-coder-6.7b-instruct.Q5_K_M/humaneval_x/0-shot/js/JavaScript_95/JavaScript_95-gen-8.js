  if(Object.keys(dict).length === 0) return false;

  let allLower = true;
  let allUpper = true;

  for(let key in dict){
    if(typeof key !== 'string') return false;
    if(key !== key.toLowerCase()) allLower = false;
    if(key !== key.toUpperCase()) allUpper = false;
 
  }

  return allLower || allUpper;
}

console.log(checkDictCase({"a":"apple", "b":"banana"}));  // should return true
console.log(checkDictCase({"a":"apple", "A":"banana", "B":"banana"})); // should return false
console.log(checkDictCase({"a":"apple", 8:"banana", "a":"apple"}));  // should return false
console.log(checkDictCase({"Name":"John", "Age":"36", "City":"Houston"}));  // should return false
console.log(checkDictCase({"STATE":"NC", "ZIP":"12345"}));  // should return true


Here's a breakdown of the code:
1. If the dictionary is empty, return false.
2. Initialize two boolean variables `allLower` and `allUpper` to true.
3. Loop through each key in the dictionary.
4. Check if the key is a string. If not, return false.
5. Check if the key is in lower case. If not, set `allLower` to false.
6. Check if the key is in upper case. If not, set `allUpper` to false.
7. After checking all keys, return true if either `allLower` or `allUpper` is true, else return false.
8. This function will return true if all keys are in lower case or all keys are in upper case, and false otherwise.
*/

```




















































