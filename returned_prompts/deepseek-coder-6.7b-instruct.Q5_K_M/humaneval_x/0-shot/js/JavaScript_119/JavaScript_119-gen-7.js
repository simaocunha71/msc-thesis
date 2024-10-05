  let str1 = lst[0];
  let str2 = lst[1];
  let stack = [];
  
  for(let i = 0; i < str1.length; i++) {
    if(str1[i] === '(') {
      stack.push(str1[i]);
    } else if(str1[i] === ')') {
      if(stack.length === 0) {
        return 'No';
      } else {
        stack.pop();
      }
    }
  }
  
  for(let i = 0; i < str2.length; i++) {
    if(str2[i] === '(') {
      stack.push(str2[i]);
    } else if(str2[i] === ')') {
      if(stack.length === 0) {
        return 'No';
      } else {
        stack.pop();
      }
    }
  }
  
  return stack.length === 0 ? 'Yes' : 'No';
}
*/

// Here we are using a stack to store the parentheses. We iterate over the strings and for each open parentheses, we push it into the stack. For each close parentheses, we check if the stack is empty, if it is, we return 'No', otherwise we pop the last element from the stack. After we have iterated over both strings, we check if the stack is empty, if it is, we return 'Yes', otherwise we return 'No'.

// The reason we are checking for open parentheses first is because we want to make sure that the number of open parentheses is equal to the number of close parentheses. If we check for close parentheses first, we might not have enough open parentheses to balance out the close parentheses.

// The time complexity of this solution is O(n), where n is the length of the string. This is because we are iterating over the string once. The space complexity is also O(n), as in the worst case, we might end up pushing all the parentheses into the stack.

// This solution works because it checks if the parentheses in the strings are balanced by using a stack. If the parenthes