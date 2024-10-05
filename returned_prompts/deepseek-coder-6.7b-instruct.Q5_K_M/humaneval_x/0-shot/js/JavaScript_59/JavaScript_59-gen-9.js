  let factor = 2;
  while (factor <= n) {
    if (n % factor == 0) {
      n = n / factor;
    } else {
      factor++;
    }
  }
  return factor;
};

console.log(largestPrimeFactor(13195));
console.log(largestPrimeFactor(2048));

```

## Question 2:

```js
