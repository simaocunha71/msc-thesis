```go
func IsMultiplyPrime(a int) bool {
    // Check if a is less than 100
    if a < 100 {
        // Create a map to store prime numbers
        primes := make(map[int]bool)
        for i := 2; i <= a; i++ {
            isPrime := true
            for j := 2; j <= int(math.Sqrt(float64(i))); j++ {
                if i%j == 0 {
                    isPrime = false
                    break
                }
            }
            if isPrime {
                primes[i] = true
            }
        }
        // Check if a is the multiplication of 3 prime numbers
        for i := 0; i < 3; i++ {
            for j := i + 1; j < 3; j++ {
                for k := j + 1; k < len(primes); k++ {
                    if a == primes[i]*primes[j]*primes[k] {
                        return true
                    }
                }
            }
        }
    }
    return false
}
```


Explanation:
This function checks if the given number `a` is the multiplication of 3 prime numbers. It first creates a map `primes` to store all prime numbers less than or equal to `a`. Then, it checks all possible combinations of 3 prime numbers in the `primes` map to see if their multiplication equals `a`. If it finds such a combination, it returns `true`. If no such combination is found, it returns `false`.

Note: This function is not efficient for large numbers because it checks all possible combinations of 3 prime numbers, which has a time complexity of O(n^2). For large numbers, a more efficient approach would be to use a sieve algorithm to find all prime numbers up to `a` and then check if `a` is the multiplication of 3 prime numbers. However, for numbers less than 100, this function should work fine.