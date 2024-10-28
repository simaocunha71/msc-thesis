```go
func IsMultiplyPrime(a int) bool {
    if a < 2 {
        return false
    }
    primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    for _, p := range primes {
        if a%p == 0 {
            a /= p
            if a == 1 {
                return true
            }
            if a < p*p {
                return false
            }
        }
    }
    return false
}
```
This function takes an integer `a` as input and checks if it is a multiplication of three prime numbers. It first checks if `a` is less than 2, in which case it returns `false`. Then it iterates through a list of prime numbers less than 100 and checks if `a` is divisible by each prime number. If it is, it divides `a` by the prime number and checks if `a` is now equal to 1, in which case it returns `true`. If `a` is not equal to 1, it checks if `a` is less than the square of the prime number, in which case it returns `false`. If none of these conditions are met, it returns `false`.