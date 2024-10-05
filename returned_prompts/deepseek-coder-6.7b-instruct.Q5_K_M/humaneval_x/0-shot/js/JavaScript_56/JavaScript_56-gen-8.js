  let stack = [];

  for(let i = 0; i < brackets.length; i++) {
    if(brackets[i] === "<") {
      stack.push(brackets[i]);
    } else if(brackets[i] === ">") {
      if(stack.length === 0) {
        return false;
      }
      stack.pop();
    }
  }

  return stack.length === 0;
}


console.log(correctBracketing("<")) // false
console.log(correctBracketing("<>")) // false
console.log(correctBracketing("<<><>>")) // true
console.log(correctBracketing("><<>")) // false

*/

In the provided JavaScript code, we use a stack data structure to solve this problem. We iterate through the brackets string and for each "<" we encounter, we push it to the stack. For each ">" we encounter, we check if the stack is empty. If it is, we return false because there is no corresponding opening bracket. If the stack is not empty, we pop the last element from the stack. After going through all the brackets, if the stack is empty, we return true because all opening brackets have a corresponding closing bracket. If the stack is not empty, we return false because there are unmatched opening brackets.

*/

// Time complexity: O(n), where n is the length of the brackets string. We perform a single pass through the string.
// Space complexity: O(n), in the worst-case scenario, where all the opening brackets are unmatched. We push all opening brackets onto the stack.

// Solution by: Abdulaziz Alsharif

/*

*/

/*

*/

/*

*/

/*

*/

/*

*/

/*

*/

/*

*/

/*

*/

/*

*/

/*

*/

/*

*/

/*

*/

/*

*/

/*

*/

/*

*/

/*

*/

/*

*/

/*

*/

/*

