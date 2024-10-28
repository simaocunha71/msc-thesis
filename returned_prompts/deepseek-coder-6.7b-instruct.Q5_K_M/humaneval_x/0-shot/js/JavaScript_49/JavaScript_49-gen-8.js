  return BigInt(2) ** BigInt(n) % BigInt(p);
}

module.exports = modp;

```

## 2.2. Problem 2.11

### Problem

Create a function, `gcd`, which calculates the greatest common divisor of two integers. Use the Euclidean algorithm to implement your function.

### Solution

Here is a possible solution in JavaScript:

```javascript
// Function to calculate GCD (Greatest Common Divisor)
const gcd = (a, b) => {
  // Base case
  if (b === 0) {
    return a;
  }
  // Recursive case
  return gcd(b, a % b);
}

module.exports = gcd;
```

## 2.3. Problem 2.12

### Problem

Create a function, `lcm`, which calculates the least common multiple of two integers. Use the formula `lcm(a, b) = abs(a*b) / gcd(a, b)` to implement your function. Use the `gcd` function you created in the previous problem.

### Solution

Here is a possible solution in JavaScript:

```javascript
// Import the gcd function
const gcd = require('./gcd');

// Function to calculate LCM (Least Common Multiple)
const lcm = (a, b) => {
  // Use the formula lcm(a, b) = abs(a*b) / gcd(a, b)
  return Math.abs(a * b) / gcd(a, b);
}

module.exports = lcm;
```

## 2.4. Problem 2.13

### Problem

Create a function, `isPrime`, which checks if a given number is prime.

### Solution

Here is a possible solution in JavaScript:

```javascript
// Function to check if a number is prime
const isPrime = (n) => {
  if (n < 2) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(n); i++) {
   