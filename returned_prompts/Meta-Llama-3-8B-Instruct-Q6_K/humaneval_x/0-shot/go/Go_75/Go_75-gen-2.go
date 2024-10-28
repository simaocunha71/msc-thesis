```go
func IsMultiplyPrime(a int) bool {
    for i := 2; i <= a; i++ {
        if IsPrime(i) && IsPrime(a/i) && IsPrime(a/i) {
            return true
        }
    }
    return false
}

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}
```


Explanation:
The function `IsMultiplyPrime` checks if the given number `a` is the product of three prime numbers. It does this by iterating over all numbers from 2 to `a` and checking if each number and its corresponding quotient are prime numbers. If it finds a pair of numbers that are prime, it returns `true`. If it doesn't find any such pair after checking all numbers, it returns `false`.

The function `IsPrime` checks if a number is prime by checking if it has any divisors other than 1 and itself. It does this by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, it returns `false`. If it doesn't find any divisors, it returns `true`.

Note: This solution has a time complexity of O(n^2) due to the nested loops in the `IsMultiplyPrime` function. This may not be efficient for large values of `a`. A more efficient solution could be achieved by using a sieve to generate all prime numbers up to a certain limit, and then checking if the given number is the product of three prime numbers from this list. However, this would require additional memory to store the sieve.