
// create a function called isPrime that checks if a number is prime
func isPrime(num int) bool {
  if num < 2 {
    return false
  }
  for i := 2; i*i <= num; i++ {
    if num%i == 0 {
      return false
    }
  }
  return true
}

// create a function called CountUpTo that returns a slice of prime numbers up to n
func CountUpTo(n int) []int {
  var primes []int
  for i := 2; i < n; i++ {
    if isPrime(i) {
      primes = append(primes, i)
    }
  }
  return primes
}

// This function uses the isPrime function to determine if a number is prime. If the number is prime, it is appended to the primes slice. The function then returns the primes slice.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

