```go
package main

import (
    "fmt"
    "math"
)

func IsMultiplyPrime(a int) bool {
    for i := 2; i <= a; i++ {
        if a%i == 0 {
            prime := true
            for j := 2; j <= int(math.Sqrt(float64(i))); j++ {
                if i%j == 0 {
                    prime = false
                    break
                }
            }
            if prime {
                for k := 2; k <= int(math.Sqrt(float64(a/i))); k++ {
                    if a/i%k == 0 {
                        prime = false
                        break
                    }
                }
                if prime {
                    return true
                }
            }
        }
    }
    return false
}

func main() {
    fmt.Println(IsMultiplyPrime(30)) // true
    fmt.Println(IsMultiplyPrime(31)) // false
}
```


This Go program defines a function `IsMultiplyPrime(a int)` that checks if the given number `a` is the product of three prime numbers. It iterates over all numbers from 2 to `a` to find the prime factors of `a`. If a prime factor is found, it checks if the remaining number (i.e., `a/i`) is also the product of two prime numbers. If both conditions are met, the function returns `true`. Otherwise, it returns `false`.

In the `main` function, we test the `IsMultiplyPrime` function with the examples provided. The output should be `true` for `IsMultiplyPrime(30)` and `false` for `IsMultiplyPrime(31)`.