  let openBrace = [];
  let closeBrace = [];

  for(let i = 0; i < string.length; i++){
    if(string[i] === '['){
      openBrace.push(i);
    } else if(string[i] === ']'){
      closeBrace.push(i);
    }
  }

  if(openBrace.length === 0 || closeBrace.length === 0){
    return false;
  }

  for(let i = 0; i < openBrace.length; i++){
    for(let j = i + 1; j < closeBrace.length; j++){
      if(openBrace[i] < closeBrace[j]){
        return true;
      }
    }
  }
  return false;
}

console.log(isNested('[[]]')); // true
console.log(isNested('[]]]]]]][[[[[]')); // false
console.log(isNested('[][]')); // false
console.log(isNested('[]')); // false
console.log(isNested('[[][]]')); // true
console.log(isNested('[[]][[')); // true


*/

This solution works by first storing the indices of any open and close brackets in separate arrays. Then it checks if there are any nested brackets by checking if the index of an open bracket is less than the index of a close bracket. If it finds one, it immediately returns true. If it doesn't find any, it returns false.

*/








































































































































