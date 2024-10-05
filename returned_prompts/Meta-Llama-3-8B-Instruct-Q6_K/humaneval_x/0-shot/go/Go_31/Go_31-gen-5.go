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
Solution:
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
The function `IsPrime` takes an integer `n` as input and returns a boolean indicating whether `n` is prime or not.

The function first checks if `n` is less than or equal to 1, in which case it returns `false` since prime numbers are greater than 1.

Then, it iterates from 2 to the square root of `n` (inclusive) and checks if `n` is divisible by any of the numbers in this range. If it is, it returns `false` since `n` is not prime.

If `n` is not divisible by any of the numbers in this range, it returns `true` since `n` is prime.

In the `main` function, we test the `IsPrime` function with different inputs and print the results. The output is as expected, with `IsPrime` correctly identifying prime and non-prime numbers.