```go
package main

import "fmt"

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(IsPrime(6))  // false
    fmt.Println(IsPrime(101))  // true
    fmt.Println(IsPrime(11))  // true
    fmt.Println(IsPrime(13441))  // true
    fmt.Println(IsPrime(61))  // true
    fmt.Println(IsPrime(4))  // false
    fmt.Println(IsPrime(1))  // false
}
```

S:
```go
package main

import "fmt"

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(IsPrime(6))  // false
    fmt.Println(IsPrime(101))  // true
    fmt.Println(IsPrime(11))  // true
    fmt.Println(IsPrime(13441))  // true
    fmt.Println(IsPrime(61))  // true
    fmt.Println(IsPrime(4))  // false
    fmt.Println(IsPrime(1))  // false
}
```

Explanation:
This Go program checks whether a given number is prime or not. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

The function `IsPrime` takes an integer `n` as input and returns a boolean indicating whether `n` is prime or not.

The function first checks if `n` is less than or equal to 1, in which case it returns `false` because prime numbers are greater than 1.

Then, it iterates from 2 to the square root of `n` (inclusive) and checks if `n` is divisible by any of these numbers. If it finds a divisor, it returns `false` because `n` is not prime.

If `n` is not divisible by any of these numbers, it returns `true` because `n` is prime.

In the `main` function, we test the `IsPrime`