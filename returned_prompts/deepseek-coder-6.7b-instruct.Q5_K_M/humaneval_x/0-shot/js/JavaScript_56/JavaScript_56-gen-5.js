  let stack = []; // create an empty stack

  for (let i = 0; i < brackets.length; i++) { // iterate through the string
    if (brackets[i] === "<") {
      stack.push(brackets[i]); // push opening brackets to the stack
    } else if (stack.length === 0) {
      return false; // if there's a closing bracket without a corresponding opening one, return false
    } else {
      stack.pop(); // if there's a matching pair, pop the opening bracket from the stack
    }
  }

  return stack.length === 0; // if the stack is empty after the loop, return true; else, return false
};

console.log(correctBracketing("<")); // false
console.log(correctBracketing("<>")); // false
console.log(correctBracketing("<<><>>")); // false
console.log(correctBracketing("><<>")); // false
console.log(correctBracketing("<><>")); // true
console.log(correctBracketing("<<><><>")); // false
console.log(correctBracketing("<<<>><>>")); // true

// Tests:
// Correctly nested brackets return true.
// Incorrectly nested brackets return false.
// Single opening bracket returns false.
// Single closing bracket returns false.
// Empty string returns true.
// String with only closing brackets returns false.
// String with only opening brackets returns false.
// String with unbalanced brackets returns false.
// String with balanced brackets returns true.
// String with unbalanced brackets and characters in between returns false.
// String with balanced brackets and characters in between returns true.
// String with unbalanced brackets at the beginning returns false.
// String with balanced brackets at the beginning returns true.
// String with unbalanced brackets at the end returns false.
// String with balanced brackets at the end returns true.
// String with unbalanced brackets in the middle returns false.
// String with balanced brackets in the middle returns true.
// String with unbalanced brackets in the middle and characters in between returns false.
// String