  if (n === 0) {
    return 1;
  }

  let result = 1;
  let base = 2;

  while (n > 0) {
    if (n % 2 === 1) {
      result = (result * base) % p;
    }
    n = Math.floor(n / 2);
    base = (base * base) % p;
  }

  return result;
};

// Tests
console.log(modp(3, 5));  // 3
console.log(modp(1101, 101));  // 2
console.log(modp(0, 101));  // 1
console.log(modp(3, 11));  // 8
console.log(modp(100, 101));  // 1

// Expected results:
// 3
// 2
// 1
// 8
// 1
```

# 3.2.4. 

```javascript
