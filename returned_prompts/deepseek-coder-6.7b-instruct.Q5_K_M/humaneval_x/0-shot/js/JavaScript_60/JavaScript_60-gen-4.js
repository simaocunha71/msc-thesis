  let sum = 0;

  for (let i = 1; i <= n; i++) {
    sum += i;
  }

  return sum;
}

console.log(sumToN(30)) // 465
console.log(sumToN(100)) // 5050
console.log(sumToN(5)) // 15
console.log(sumToN(10)) // 55
console.log(sumToN(1)) // 1
```

## Task 2

Write a JavaScript function that takes an array of integers and returns the sum of the squares of those integers.

Example:
```javascript
squareSum([1, 2, 3, 4]) // should return 30
// because 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = 30
```

```javascript
