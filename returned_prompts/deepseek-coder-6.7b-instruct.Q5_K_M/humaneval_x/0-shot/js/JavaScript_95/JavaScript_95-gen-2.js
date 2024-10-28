  if(Object.keys(dict).length === 0){
    return false;
  }
  let lower = 0;
  let upper = 0;
  for(let key in dict){
    if(key == key.toLowerCase()){
      lower += 1;
    }
    if(key == key.toUpperCase()){
      upper += 1;
    }
  }
  if(lower == Object.keys(dict).length || upper == Object.keys(dict).length){
    return true;
  }
  return false;
}

console.log(checkDictCase({"a":"apple", "b":"banana"})); // true
console.log(checkDictCase({"a":"apple", "A":"banana", "B":"banana"})); // false
console.log(checkDictCase({"a":"apple", 8:"banana", "a":"apple"})); // false
console.log(checkDictCase({"Name":"John", "Age":"36", "City":"Houston"})); // false
console.log(checkDictCase({"STATE":"NC", "ZIP":"12345"})); // true

*/
/*
  Explain your solution:
  In the function `checkDictCase`, firstly, we check if the dictionary is empty, if so, return false.
  Then we count the keys that are all lower case and keys that are all upper case. 
  If either count is equal to the total number of keys in the dictionary, 
  we return true indicating that all keys are either all lower case or all upper case. 
  Otherwise, we return false.
*/

/*
  This solution works by iterating over the keys in the dictionary and comparing them to their lower case and upper case counterparts. 
  If they are equal, it means the key is in lower case or upper case. 
  The function then checks if the total count of keys in lower case or upper case is equal to the total number of keys in the dictionary, 
  if so, it returns true indicating that all keys are either in lower case or upper case.
  If the dictionary is empty, the function returns false.
*/

/*
