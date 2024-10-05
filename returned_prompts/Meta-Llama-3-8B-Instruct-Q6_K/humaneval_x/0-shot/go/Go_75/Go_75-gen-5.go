```go
package main

import (
    "fmt"
)

func IsMultiplyPrime(a int) bool {
    for i := 2; i <= a; i++ {
        for j := 2; j <= a; j++ {
            for k := 2; k <= a; k++ {
                if i*j*k == a {
                    if IsPrime(i) && IsPrime(j) && IsPrime(k) {
                        return true
                    }
                }
            }
        }
    }
    return false
}

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
    fmt.Println(IsMultiplyPrime(30))  // true
    fmt.Println(IsMultiplyPrime(100)) // false
}
```

Explanation:
The function `IsMultiplyPrime(a int)` checks if the given number `a` is the multiplication of 3 prime numbers. It does this by iterating over all possible combinations of numbers from 2 to `a`, and checks if the product of these numbers is equal to `a`. If the product is equal to `a` and all the numbers are prime, it returns `true`. Otherwise, it returns `false`.

The function `IsPrime(n int)` checks if a given number `n` is prime. It does this by iterating over all numbers from 2 to the square root of `n`, and checks if `n` is divisible by any of these numbers. If `n` is divisible by any of these numbers, it returns `false`. Otherwise, it returns `true`.

In the `main` function, we test the `IsMultiplyPrime` function with the numbers 30 and 100. The output is `true` for 30 (because 30 is the multiplication of 2, 3, and 5, which are all prime numbers) and `false` for 100 (because 100 is not the multiplication of 3 prime numbers).