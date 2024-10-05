  let stack = [];
  for(let i=0; i<string.length; i++){
    if(string[i] === '['){
      stack.push(string[i]);
    } else {
      if(stack.length === 0){
        return false;
      } else {
        stack.pop();
      }
    }
  }
  return stack.length !== 0 ? false : true;
}


console.log(isNested('[[]]')); // ➞ true
console.log(isNested('[]]]]]]][[[[[]')); // ➞ false
console.log(isNested('[][]')); // ➞ false
console.log(isNested('[]')); // ➞ false
console.log(isNested('[[][]]')); // ➞ true
console.log(isNested('[[]][[')); // ➞ true

*/

In this code, we use a stack to track the brackets. When we see an opening bracket, we push it into the stack. When we see a closing bracket, we pop the top element from the stack. If the stack is empty at the end, it means that there is no nested bracket. If there are still elements in the stack at the end, it means that there is at least one unclosed bracket, so we return false.

*/

/*
  In the end, if the stack is empty, it means that all brackets are properly nested and we return true. Otherwise, it means that there is at least one unclosed bracket and we return false.
*/

/*
  This code works by iterating over the input string and using a stack to keep track of the brackets. When an opening bracket is encountered, it is pushed onto the stack. When a closing bracket is encountered, it is compared to the top of the stack. If they match, the brackets are properly nested, and the opening bracket is removed from the stack. If they do not match, or if there are no brackets left on the stack, the function returns false. If the stack is empty at the end, the function returns true, indicating that all brackets were properly nested.
*/

/*
  The