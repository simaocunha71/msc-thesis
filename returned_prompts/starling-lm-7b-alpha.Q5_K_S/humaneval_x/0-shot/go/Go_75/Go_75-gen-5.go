
```go
func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    if n == 2 {
        return true
    }
    if n%2 == 0 {
        return false
    }
    for i := 3; i * i <= n; i += 2 {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func IsMultiplyPrime(a int) bool {
    var i, j, k int
    for i = 2; i < a; i++ {
        for j = i + 1; j < a; j++ {
            for k = j + 1; k < a; k++ {
                if isPrime(i) && isPrime(j) && isPrime(k) && i*j*k == a {
                    return true
                }
            }
        }
    }
    return false
}
```

In this function, we check if a number is the multiplication of three prime numbers.
To do this, we check every possible combination of three numbers, from 2 to a, if they are prime and if their product is equal to a.

It's not the most efficient solution, but it's simple to understand.

```go
func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    if n == 2 {
        return true
    }
    if n%2 == 0 {
        return false
    }
    for i := 3; i * i <= n; i += 2 {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func IsMultiplyPrime(a int) bool {
    var i, j, k int
    for i = 2; i < a; i++ {
        for j = i + 1; j < a; j++ {
            for k = j + 1; k < a; k++ {
                if isPrime(i) && isPrime(j) && is