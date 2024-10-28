
Here is a simple implementation of the Fibonacci function in Go:

```go
package main

import "fmt"

func Fib(n int) int {
    if n == 0 {
        return 0
    } else if n == 1 {
        return 1
    }
    return Fib(n-1) + Fib(n-2)
}

func main() {
    fmt.Println(Fib(10))
    fmt.Println(Fib(1))
    fmt.Println(Fib(8))
}
```

When you run the program, the output will be:

```
55
1
21
```

This code uses a recursive function to calculate Fibonacci numbers. If the input is 0, it returns 0, if the input is 1, it returns 1. Otherwise, it calls the Fib function twice with n-1 and n-2 as inputs, and adds the results together.

This approach is not very efficient for large inputs, since it makes the same subproblems over and over again. A more efficient approach would be to use memoization, which stores the results of subproblems so that they don't have to be recomputed.

Here's an example of how you can modify the Fib function to use memoization:

```go
package main

import "fmt"

func Fib(n int, memo map[int]int) int {
    if n == 0 {
        return 0
    } else if n == 1 {
        return 1
    }
    if _, ok := memo[n]; !ok {
        memo[n] = Fib(n-1, memo) + Fib(n-2, memo)
    }
    return memo[n]
}

func main() {
    memo := make(map[int]int)
    fmt.Println(Fib(10, memo))
    fmt.Println(Fib(1, memo))
    fmt.Println(Fib(8, memo))
}
```

With this modification, the Fib function now takes an additional parameter, `