  for(let i = n - 1; i > 0; i--) {
    if(n % i === 0) {
      return i;
    }
  }
}

console.log(largestDivisor(15));
```

The function largestDivisor finds the largest number that divides n evenly, smaller than n, by starting at n - 1 and going down to 1, checking each time if n is divisible by the current number i. If it is, it returns i, because i is the largest number that divides n evenly. If no such number is found, the function returns undefined.

The function uses a for loop to iterate over the numbers from n - 1 down to 1. It checks if n is divisible by the current number i by using the modulus operator %. If n is divisible by i (i.e., n % i is 0), the function returns i as the largest divisor. If no such number i is found, the function returns undefined.

The time complexity of the function is O(n) because in the worst case, it needs to iterate over all numbers from n - 1 down to 1.

The space complexity of the function is O(1), because it uses a fixed amount of space to store the variables n, i, and the return value, regardless of the size of n.

```js
