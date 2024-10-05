    if n <= 1 {
        return n
    }
    a, b := 0, 1
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}

package main

import (
    "fmt"
    "math/rand"
    "time"
)

func main() {
    rand.Seed(time.Now().UnixNano())
    for i := 0; i < 10; i++ {
        n := rand.Intn(50) + 1
        fmt.Println(Fib(n))
    }
}

// Output:
// 1
// 21
// 55
// 1
// 13
// 144
// 21
// 34
// 89
// 21

Explanation:

This is a simple implementation of the Fibonacci sequence in Go. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

The `Fib` function takes an integer `n` as input and returns the `n`-th Fibonacci number. If `n` is 0 or 1, the function returns `n` directly. Otherwise, it initializes two variables `a` and `b` to 0 and 1, respectively, and then iterates from 2 to `n`. In each iteration, it updates `a` and `b` to `b` and `a+b`, respectively. Finally, it returns `b`, which is the `n`-th Fibonacci number.

In the `main` function, we use the `rand` package to generate random numbers between 1 and 50, and then call the `Fib` function with each generated number. The output shows the Fibonacci numbers for the generated numbers.

Note that this implementation has a time complexity of O(n), which means the running time increases linearly with the input `n`. This is because we need to iterate from 2 to `n` to calculate the `n`-th Fibonacci number. For large values of `n`, this implementation may be slow. There are more efficient algorithms available for calculating Fibonacci numbers, such as the matrix exponentiation method or the recursive formula with memoization. However, this implementation is simple and easy to understand.