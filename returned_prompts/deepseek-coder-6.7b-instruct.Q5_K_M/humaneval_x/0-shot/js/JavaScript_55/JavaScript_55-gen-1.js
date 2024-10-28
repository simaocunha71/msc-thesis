  if (n <= 2) return 1;
  let fibNums = [1, 1];
  for (let i = 2; i < n; i++) {
    fibNums.push(fibNums[i-1] + fibNums[i-2]);
  }
  return fibNums.pop();
}

console.log(fib(10)); // 55
console.log(fib(1)); // 1
console.log(fib(8)); // 21
```

## Problem 11

```javascript
