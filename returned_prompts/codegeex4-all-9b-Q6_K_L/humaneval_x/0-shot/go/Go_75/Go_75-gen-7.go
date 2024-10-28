```go
func IsMultiplyPrime(a int) bool {
    // Check if a is less than 2
    if a < 2 {
        return false
    }

    // Check if a is a prime number
    isPrime := true
    for i := 2; i*i <= a; i++ {
        if a%i == 0 {
            isPrime = false
            break
        }
    }

    // If a is a prime number, return false
    if isPrime {
        return false
    }

    // Check if a is the multiplication of 3 prime numbers
    for i := 2; i <= a/2; i++ {
        for j := i + 1; j <= a/i; j++ {
            for k := j + 1; k <= a/(i*j); k++ {
                if i*j*k == a {
                    return true
                }
            }
        }
    }

    return false
}
```
