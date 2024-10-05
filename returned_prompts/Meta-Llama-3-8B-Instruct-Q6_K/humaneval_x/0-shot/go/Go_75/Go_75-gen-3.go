```go
func IsMultiplyPrime(a int) bool {
    // Check if a is less than 100
    if a < 100 {
        // Generate all prime numbers less than or equal to a
        primes := make([]bool, a+1)
        primes[0] = primes[1] = false
        for i := 2; i <= a; i++ {
            primes[i] = true
        }
        for i := 2; i*i <= a; i++ {
            if primes[i] {
                for j := i * i; j <= a; j += i {
                    primes[j] = false
                }
            }
        }
        // Check if a can be expressed as the product of three prime numbers
        for i := 2; i <= a; i++ {
            for j := i; j <= a/i; j++ {
                k := a / (i * j)
                if primes[i] && primes[j] && primes[k] {
                    return true
                }
            }
        }
        return false
    } else {
        // If a is greater than or equal to 100, the function should return false
        return false
    }
}
```


The solution checks if the given number `a` can be expressed as the product of three prime numbers. It first generates all prime numbers less than or equal to `a`. Then it checks if `a` can be expressed as the product of three prime numbers by iterating over all possible combinations of prime numbers.

The time complexity of this solution is O(a^2), where `a` is the input number. This is because we are iterating over all prime numbers less than or equal to `a`, and then iterating over all possible combinations of prime numbers.

The space complexity is O(a), as we are storing all prime numbers less than or equal to `a` in a boolean array.