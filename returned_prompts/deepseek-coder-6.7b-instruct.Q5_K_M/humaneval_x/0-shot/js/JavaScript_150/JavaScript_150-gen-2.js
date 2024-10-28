  let isPrime = true;

  if (n === 1) {
    isPrime = false;
  } else if (n > 1) {
    for(let i = 2; i < n; i++) {
      if(n % i === 0) {
        isPrime = false;
        break;
      }
    }
  }

  return isPrime ? x : y;
}

console.log(xOrY(7, 34, 12)); // 34
console.log(xOrY(15, 8, 5)); // 5
```

## 2. Write a JavaScript function that will convert a given integer number to its word representation.

Example: 
Input: 123
Output: "one hundred and twenty-three"

```javascript
