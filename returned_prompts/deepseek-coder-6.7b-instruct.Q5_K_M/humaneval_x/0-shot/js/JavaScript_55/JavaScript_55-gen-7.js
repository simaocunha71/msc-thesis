  if (n <= 2) {
    return 1;
  }
  let prev = 1;
  let curr = 1;
  for (let i = 3; i <= n; i++) {
    let temp = curr;
    curr += prev;
    prev = temp;
  }
  return curr;
};

console.log(fib(10)); // 55
console.log(fib(1)); // 1
console.log(fib(8)); // 21
```

## Problem 2:

Write a function that takes two numbers and returns the greatest common divisor of those two numbers.

```javascript
