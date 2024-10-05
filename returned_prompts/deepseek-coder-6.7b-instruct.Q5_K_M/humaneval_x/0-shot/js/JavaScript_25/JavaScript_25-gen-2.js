  const factors = [];
  let divisor = 2;

  while (divisor <= n) {
    if (n % divisor === 0) {
      factors.push(divisor);
      n /= divisor;
    } else {
      divisor++;
    }
  }

  return factors;
}

console.log(factorize(8));  // [2, 2, 2]
console.log(factorize(25)); // [5, 5]
console.log(factorize(70)); // [2, 5, 7]

// The solution works by continuously dividing the input number by the smallest possible divisor (starting from 2) until it's fully factorized.
// If the number isn't divisible by the divisor, the divisor is incremented. This process continues until the number is fully factorized.
// The factors are returned in the order from smallest to largest.
// Each of the factors appears number of times corresponding to how many times it appeares in factorization.
```

---

### 