
/* 
1. split the string into an array of characters
2. loop through the array of characters and look for parentheses
3. if you find a left parentheses, add it to a stack
4. if you find a right parentheses, pop the stack and add the parentheses to the result array
5. when done with the array of characters, return the result array
*/
const separateParenGroups = (paren_string) => {
  let paren_array = paren_string.split('');
  let paren_stack = [];
  let result = [];
  
  for (let i = 0; i < paren_array.length; i++) {
    if (paren_array[i] === '(') {
      paren_stack.push(paren_array[i]);
    } else if (paren_array[i] === ')') {
      let paren = paren_stack.pop();
      result.push(paren);
    }
  }
  return result;
};