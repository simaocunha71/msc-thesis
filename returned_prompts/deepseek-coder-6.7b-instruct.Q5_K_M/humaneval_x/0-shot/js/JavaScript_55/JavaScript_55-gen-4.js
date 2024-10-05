  if (n === 1) {
    return 1;
  }
  if (n === 0) {
    return 0;
  }
  let fibNums = [0, 1];
  for (let i = 2; i <= n; i++) {
    fibNums[i] = fibNums[i - 1] + fibNums[i - 2];
  }
  return fibNums[n];
}

console.log(fib(10)); //55
console.log(fib(1)); //1
console.log(fib(8)); //21
```

In this version, we first handle the base cases of `n` being `1` or `0`, then we create an array `fibNums` to store the Fibonacci sequence. We then use a `for` loop to fill `fibNums` up to the `n`th Fibonacci number. Finally, we return the `n`th Fibonacci number from `fibNums`.

This version of the function is more efficient than the previous one because it only needs to loop through the sequence once, instead of recalculating each Fibonacci number.

In terms of time complexity, this version is O(n). The space complexity is also O(n) as we store all Fibonacci numbers up to `n`.

### Version 3: Space-Efficient Fibonacci Function

This version of the function only stores the last two Fibonacci numbers at any given time, rather than all of them. This makes it more space-efficient:

```javascript
