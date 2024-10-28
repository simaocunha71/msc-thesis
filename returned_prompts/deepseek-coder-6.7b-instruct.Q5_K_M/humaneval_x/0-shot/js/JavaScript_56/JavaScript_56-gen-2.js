  let stack = [];

  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === "<") {
      stack.push(brackets[i]);
    } else if (brackets[i] === ">") {
      if (stack.length === 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }

  return stack.length === 0;
};

console.log(correctBracketing("<")); // false
console.log(correctBracketing("<>")); // false
console.log(correctBracketing("<<><>>")); // false
console.log(correctBracketing("><<>")); // false

// Correct bracket examples
console.log(correctBracketing("<>><")); // true
console.log(correctBracketing("<><>")); // true
```

## Exercise 10.5

