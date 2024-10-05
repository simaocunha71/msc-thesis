
    if n < 2 {
        return false
    }
    if n == 2 {
        return true
    }
    if n % 2 == 0 {
        return false
    }
    sqrt := int(math.Sqrt(float64(n)))
    for i := 3; i <= sqrt; i += 2 {
        if n % i == 0 {
            return false
        }
    }
    return true
}

// Find the largest prime factor of a given number.
// 
// >>> LargestPrimeFactor(13195)
// 29
func LargestPrimeFactor(n int) int {

B:

    if n < 2 {
        return -1
    }
    largest := 2
    for i := 2; i * i <= n; i++ {
        if n % i == 0 {
            if IsPrime(i) {
                largest = i
            }
            if IsPrime(n / i) {
                largest = n / i
            }
        }
    }
    return largest
}

// Return the sum of all primes below a given number.
// 
// >>> SumOfPrimes(10)
// 17
func SumOfPrimes(n int) int {

C:

    if n < 2 {
        return -1
    }
    sum := 0
    for i := 2; i < n; i++ {
        if IsPrime(i) {
            sum += i
        }
    }
    return sum
}

```

## Explanation

This program contains three functions:

- `IsPrime(n int) bool`: This function checks if a given number is a prime number. It returns `true` if the number is prime and `false` otherwise. It does this by first checking if the number is less than 2 (in which case it is not prime), then checking if the number is even (in which case it is not prime), and finally checking if the number has any divisors other than 1 and itself (in which case it is not prime).

- `LargestPr