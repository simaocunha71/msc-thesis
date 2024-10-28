  const isPrime = (num) => {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  }

  return isPrime(n) ? x : y;
}

console.log(xOrY(7, 34, 12));  // 34
console.log(xOrY(15, 8, 5));   // 5
```

## 12. Write a JavaScript function that will return the sum of the digits of a number.

```javascript
