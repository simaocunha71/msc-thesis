To check if a number is prime, we need to iterate through all the numbers from 2 to the square root of the number and see if any of them evenly divide the number.

Here's a step-by-step breakdown of the solution:

1. Initialize a variable `i` to 2.
2. Check if `i` is less than or equal to the square root of the given number `n`.
3. If `i` is less than or equal to the square root of `n`, check if `n` is divisible by `i` using the modulo operator `%`. If `n % i == 0`, it means `n` is divisible by `i` and is not a prime number. Return `false`.
4. If `i` is greater than the square root of `n`, it means all the factors of `n` have been checked. Return `true` to indicate that `n` is a prime number.
5. Increment `i` by 1 and go back to step 2.
6. Repeat steps 2-5 until all factors of `n` have been checked.

Here's the implementation of the `IsPrime` function in Go:

```go
package main

import (
    "fmt"
    "math"
)

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    if n <= 3 {
        return true
    }
    if n%2 == 0 || n%3 == 0 {
        return false
    }
    i := 5
    for i * i <= n {
        if n%i == 0 || n%(i + 2) == 0 {
            return false
        }
        i += 6
    }
    return true
}
```

You can test the function using the provided examples:

```go
fmt.Println(IsPrime(6))    // false
fmt.Println(IsPrime(101))  // true
fmt.Println(IsPrime(11))   // true
fmt.Println(IsPrime(13441)) // true
fmt.Println(IsPrime