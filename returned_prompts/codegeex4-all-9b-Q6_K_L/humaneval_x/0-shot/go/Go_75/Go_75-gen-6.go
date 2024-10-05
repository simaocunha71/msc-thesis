To determine if a number is the multiplication of three prime numbers, we need to factorize the number and check if it can be expressed as the product of exactly three distinct prime factors. Here's a step-by-step breakdown of the algorithm:

1. **Check if the number is less than 2**: If the number is less than 2, it cannot be a product of three prime numbers, so return `false`.
2. **Iterate through potential divisors**: Start with the smallest prime number, which is 2, and check if it divides `a` without a remainder.
3. **Count divisors**: If it does, increment the divisor count and divide `a` by the divisor.
4. **Check for multiple prime factors**: If at any point the divisor count exceeds 3, return `false` because the number cannot be the product of three distinct primes.
5. **Move to the next potential prime**: If the divisor is 2 and it doesn't divide `a`, increment the divisor to 3 (the next prime number) and continue the process.
6. **Repeat until `a` is 1**: Continue finding prime divisors until `a` is reduced to 1 or you've found three prime divisors.
7. **Check for exactly three prime factors**: If `a` is reduced to 1 and you've found exactly three prime divisors, return `true`. Otherwise, return `false`.

Here's the Go code implementing the above algorithm:

```go
func IsMultiplyPrime(a int) bool {
    if a < 2 {
        return false
    }
    var count int
    for i := 2; i <= a; i++ {
        for a%i == 0 {
            count++
            if count > 3 {
                return false
            }
            a /= i
        }
        if i*i > a {
            break
        }
    }
    return count == 3 && a == 1
}
```

This function will correctly determine if the given number `a` is the product of exactly three prime numbers.