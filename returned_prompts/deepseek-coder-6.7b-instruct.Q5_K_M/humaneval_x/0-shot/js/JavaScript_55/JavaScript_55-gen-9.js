  if (n <= 2) return 1;

  let fibNums = [1, 1];

  for (let i = 2; i < n; i++) {
    fibNums[i] = fibNums[i-1] + fibNums[i-2];
  }

  return fibNums[n-1];
}

console.log(fib(10));
console.log(fib(1));
console.log(fib(8));
```

## 5. 数组的反转

```javascript
