
// First, we need to create a helper function to check if a number is prime or not

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i * i <= n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}

// Then, we can use this helper function to check if the length of the string is prime

func PrimeLength(s string) bool {
    return isPrime(len(s))
}

// The helper function isPrime checks if a number is prime by iterating from 2 to the square root of the number
// and checking if the number is divisible by any of these values. If it is, then it is not a prime number.
// If the number is not divisible by any of these values, then it is a prime number.
```

---

## Question 6

Write a function that takes two integers and returns a boolean. The function should return true if the sum of the integers is divisible by 3, and false otherwise.

```go
