
Here's a function that takes in three integer parameters: n, x, and y. It returns the value of x if n is a prime number, and the value of y otherwise.

```go
package main

import (
    "fmt"
)

func XOrY(n, x, y int) int {
    if isPrime(n) {
        return x
    }
    return y
}

func isPrime(n int) bool {
    for i := 2; i*i <= n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(XOrY(7, 34, 12))    // 34
    fmt.Println(XOrY(15, 8, 5))     // 5
}
```

In this program, the `XOrY` function checks if the number `n` is a prime number by calling the `isPrime` function. If it is a prime number, it returns the value of `x`, otherwise it returns the value of `y`. The `isPrime` function checks if a number `n` is prime by iterating from 2 to the square root of `n` and checking if `n` is divisible by any of these numbers. If it is divisible by any of them, it is not a prime number, and the function returns `false`. If none of the iterations find a divisor, the function returns `true`. 

The main function demonstrates the usage of the `XOrY` function by calling it with different inputs and printing the results.

```go
func main() {
    fmt.Println(XOrY(7, 34, 12))    // 34
    fmt.Println(XOrY(15, 8, 5))     // 5
}
```

For the given inputs, the function returns `34` for `XOrY(7, 34, 12)` and `5` for `XOrY(15, 8, 5)`.

```go
// A simple