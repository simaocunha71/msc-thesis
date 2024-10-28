
To solve this problem we need to understand the concept of modular exponentiation.

Modular exponentiation is a way of efficiently calculating a power modulo a given modulus. In this case, we want to calculate 2^n modulo p. Here is how we can do it:

1. Initialize a variable called `res` to 2.
2. Initialize a variable called `x` to `n`.
3. While `x` is greater than 0:
   - If `x` is odd, multiply `res` by 2 and take the modulo `p`.
   - If `x` is even, multiply `res` by 1 and take the modulo `p`.
   - Increment `res` by 1 and decrement `x` by 1.
4. Return `res`.

Here is the code:

```go
package main

import "fmt"

func Modp(n, p int) int {
    res := 2
    x := n
    for x > 0 {
        if x%2 == 1 {
            res = (res * 2) % p
        } else {
            res = (res * 1) % p
        }
        res++
        x--
    }
    return res
}

func main() {
    fmt.Println(Modp(3, 5))
    fmt.Println(Modp(1101, 101))
    fmt.Println(Modp(0, 101))
    fmt.Println(Modp(3, 11))
    fmt.Println(Modp(100, 101))
}
```

In this code, we define a function called `Modp` that takes two integers `n` and `p`. It initializes a variable called `res` to 2 and a variable called `x` to `n`. It then enters a loop that runs as long as `x` is greater than 0.

Inside the loop, it checks if `x` is odd. If it is, it multiplies `res` by 2 and takes the modulo `p`. If `x` is even, it multiplies `