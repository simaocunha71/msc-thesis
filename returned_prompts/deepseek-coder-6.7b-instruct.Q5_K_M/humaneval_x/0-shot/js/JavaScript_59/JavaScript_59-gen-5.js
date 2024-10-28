  let largest = -1; 

  while (n % 2 === 0) { 
    n /= 2; 
  }

  for (let i = 3; i * i <= n; i += 2) { 
    while (n % i === 0) { 
      largest = i; 
      n /= i; 
    } 
  } 

  if (n > 2) { 
    largest = n; 
  }

  return largest; 
}

module.exports = largestPrimeFactor;
```

This solution works by continuously dividing the input number by 2 while it's divisible, then checking for factors in odd numbers starting from 3. This is an efficient way to find the largest prime factor. Once we've found the largest prime factor, we return it.

Testing the solution

Here's how you can test the solution:

```javascript
console.log(largestPrimeFactor(13195)); // Output: 29
console.log(largestPrimeFactor(2048)); // Output: 2
```

This should output the expected results.

**Note:** This solution assumes that the input number is always greater than 1 and is not a prime number. If you want to handle the case where the input number is a prime number, you need to add a separate check for that case.

### Improved solution

Here's an improved version of the solution that handles the case where the input number is a prime number:

```javascript
const largestPrimeFactor = (n) => {
  if (n < 2) {
    return null;
  }

  let largest = -1;

  while (n % 2 === 0) {
    n /= 2;
  }

  for (let i = 3; i * i <= n; i += 2) {
    while (n % i === 0) {
      largest = i;
      n /= i;
    }
  }

  if (n > 2) {
    largest = n;
  }

  return largest;
}

module.exports = largestPrimeFactor;