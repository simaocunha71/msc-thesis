  const stack = [];

  for(let i = 0; i < brackets.length; i++) {
    if(brackets[i] === '(') {
      stack.push(brackets[i]);
    } else if(brackets[i] === ')') {
      if(stack.length === 0) {
        return false;
      }
      stack.pop();
    }
  }

  return stack.length === 0;
}

console.log(correctBracketing("(")); // false
console.log(correctBracketing("()")); // true
console.log(correctBracketing("(()())")); // true
console.log(correctBracketing(")(()")); // false
```

## 5. Fibonacci Series

