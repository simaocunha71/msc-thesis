  let result = 1;

  for(let i = 1; i <= n; i++) {
    let factorial = 1;

    for(let j = 1; j <= i; j++) {
      factorial *= j;
    }

    result *= factorial;
  }

  return result;
}

console.log(specialFactorial(4)); // 288
console.log(specialFactorial(5)); // 34560
console.log(specialFactorial(6)); // 24883200
```



## 3. Write a function that returns the nth Fibonacci number in the sequence.

```javascript
