
To solve this problem, we can use a dynamic programming approach, i.e., memoization. We will create a map called `memo` to store the results of all Fibonacci numbers that we've computed so far.

Here's the implementation of the `Fib` function using memoization:

```go
package main

import "fmt"

func Fib(n int) int {
    memo := make(map[int]int)
    return fibHelper(n, &memo)
}

func fibHelper(n int, memo *map[int]int) int {
    if n <= 1 {
        return n
    }

    if _, ok := (*memo)[n]; !ok {
        (*memo)[n] = fibHelper(n-1, memo) + fibHelper(n-2, memo)
    }
    return (*memo)[n]
}
```

You can use the `Fib` function as follows:

```go
fmt.Println(Fib(10))  // prints 55
fmt.Println(Fib(1))   // prints 1
fmt.Println(Fib(8))   // prints 21
```

In the `Fib` function, we first create an empty map called `memo`. Then, we call the `fibHelper` function with the input `n` and the address of the `memo` map. The `fibHelper` function is a recursive function that computes the Fibonacci number for the given input `n`.

In the `fibHelper` function, we first check if the Fibonacci number for `n` is already present in the `memo` map. If it is, we simply return the value from the map. If it's not, we compute the Fibonacci number for `n` by recursively calling `fibHelper` with `n-1` and `n-2` and summing up the results. Then, we store the result in the `memo` map for future use.

By using memoization, we avoid redundant computations and improve the performance of the `Fib` function.

```go
package main

