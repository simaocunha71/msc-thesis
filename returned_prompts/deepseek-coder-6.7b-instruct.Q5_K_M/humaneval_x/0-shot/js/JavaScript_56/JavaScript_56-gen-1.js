  let stack = [];

  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === '<') {
      stack.push(brackets[i]);
    } else {
      if (stack.length === 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }

  return stack.length === 0;
}

// Test cases
console.log(correctBracketing("<")); // false
console.log(correctBracketing("<>")); // false
console.log(correctBracketing("<<><>>")); // true
console.log(correctBracketing("><<>")); // false

*/

// Solution

/*

In the problem, we are given a string of brackets "<" and ">". The task is to check whether every opening bracket "<" has a corresponding closing bracket ">". 

We can use a stack data structure to solve this problem. We iterate through the string and for each character, if it is an opening bracket "<", we push it into the stack. If it is a closing bracket ">", we pop the top element from the stack. If the stack is empty at the end, it means that every opening bracket has a corresponding closing bracket, so we return true. Otherwise, we return false.

*/

// Pseudocode

/*

function correctBracketing(brackets) {
  let stack = [];

  for each character in brackets {
    if character is "<" {
      push character into stack
    } else {
      if stack is empty {
        return false
      } else {
        pop top element from stack
      }
    }
  }

  if stack is not empty {
    return false
  } else {
    return true
  }
}

*/

// Time complexity

/*

The time complexity of this solution is O(n), where n is the length of the string. This is because we are iterating through the string once, and for each character we are performing a constant amount of work (pushing onto the stack or popping from the stack).

*/