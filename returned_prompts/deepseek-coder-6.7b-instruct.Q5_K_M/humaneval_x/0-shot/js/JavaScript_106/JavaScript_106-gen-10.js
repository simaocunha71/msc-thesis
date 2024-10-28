  let arr = []
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      let fact = 1;
      for (let j = 1; j <= i; j++) {
        fact *= j;
      }
      arr.push(fact);
    } else {
      let sum = 0;
      for (let j = 1; j <= i; j++) {
        sum += j;
      }
      arr.push(sum);
    }
  }
  return arr;
}

console.log(f(5));

// the complexity of this function is O(n^2) as we are iterating through n elements and for each element we are iterating through n elements again.
```

# Question 2

```javascript
