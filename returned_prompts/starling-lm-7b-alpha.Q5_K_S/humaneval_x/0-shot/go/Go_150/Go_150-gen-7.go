
To solve this problem, we can follow these steps:

1. Check if the given number `n` is prime or not.
2. If `n` is prime, return `x`, otherwise return `y`.

To check if `n` is prime or not, we can use the following algorithm:

1. If `n` is less than 2, it is not prime. So, we return `false`.
2. If `n` is equal to 2, it is prime. So, we return `true`.
3. If `n` is even, it is not prime. So, we return `false`.
4. Otherwise, we iterate from 2 to `n-1` and check if `n` is divisible by any number in this range. If it is divisible by any number, it is not prime. So, we return `false`.
5. If none of the above conditions are met, `n` is prime. So, we return `true`.

Now, let's implement the above algorithm in Go:

```go
package main

import "fmt"

func XOrY(n, x, y int) int {
    if n < 2 {
        return y
    }
    if n == 2 {
        return x
    }
    if n%2 == 0 {
        return y
    }
    for i := 2; i < n; i++ {
        if n%i == 0 {
            return y
        }
    }
    return x
}

func main() {
    fmt.Println(XOrY(7, 34, 12)) // 34
    fmt.Println(XOrY(15, 8, 5))  // 5
}
```

In the `XOrY` function, we first check if `n` is less than 2, and if it is, we return `y`. Then, we check if `n` is equal to 2, and if it is, we return `x`. After that, we check if `n` is even, and if it is, we return `y`. If none of the above conditions are met, we iterate from 2 to `n-1`