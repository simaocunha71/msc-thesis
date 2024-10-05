  if(n <= 1 || !Number.isInteger(n)) {
    return y;
  }
  for(let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if(n % i === 0) {
      return y;
    }
  }
  return x;
}

console.log(xOrY(7, 34, 12)); // 34
console.log(xOrY(15, 8, 5));  // 5
console.log(xOrY(2, 10, 20)); // 10
console.log(xOrY(3, 10, 20)); // 10
console.log(xOrY(4, 10, 20)); // 20
console.log(xOrY(5, 10, 20)); // 10
```

### Task 2:

```javascript
