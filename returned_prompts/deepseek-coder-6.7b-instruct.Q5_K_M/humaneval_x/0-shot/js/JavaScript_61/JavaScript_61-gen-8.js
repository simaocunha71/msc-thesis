  let stack = [];

  for(let i = 0; i < brackets.length; i++) {
    if(brackets[i] === "(") {
      stack.push(brackets[i]);
    } else if(brackets[i] === ")") {
      if(stack.length === 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }

  return stack.length === 0;
}

console.log(correctBracketing("("));
console.log(correctBracketing("()"));
console.log(correctBracketing("(()())"));
console.log(correctBracketing(")(()"));

This solution uses a stack data structure to keep track of opening brackets. Every time we encounter a closing bracket, we remove the most recent opening bracket from the stack. If the stack ends up empty at the end, that means all brackets were properly matched and we return true. If there are any leftover opening brackets in the stack, that means there were unmatched opening brackets and we return false.

This solution has a time complexity of O(n) and a space complexity of O(n) as it uses a stack to keep track of the opening brackets and it iterates through the string once.
*/

// The function correctBracketing checks if every opening bracket has a corresponding closing bracket.
const correctBracketing = (brackets) => {
  // Initialize an empty stack
  let stack = [];

  // Iterate through each character in the brackets string
  for(let i = 0; i < brackets.length; i++) {
    // If the character is an opening bracket, push it onto the stack
    if(brackets[i] === "(") {
      stack.push(brackets[i]);
    } 
    // If the character is a closing bracket
    else if(brackets[i] === ")") {
      // If the stack is empty, that means there is no matching opening bracket
      if(stack.length === 0) {
        return false;
      } 
      // If the stack is not empty, pop the top element from the stack
