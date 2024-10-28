  let factors = [];
  // The smallest prime number
  let divisor = 2;

  while(n>1){
      while(n % divisor === 0){
          factors.push(divisor);
          n = n / divisor;
      }
      divisor++;
  }
  return factors;
}
console.log(factorize(8));
console.log(factorize(25));
console.log(factorize(70));
```

## 3. Fibonacci sequence

Write a function to generate the nth Fibonacci number. The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it.

```javascript
