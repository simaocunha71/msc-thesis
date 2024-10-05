
To solve this problem, we can use dynamic programming to store previously computed fibonacci numbers in an array. This way, instead of computing each fibonacci number from scratch, we can use the previously computed number.

Here's a possible solution in Go:

```go
package main

import "fmt"

func Fib(n int) int {
    if n <= 1 {
        return n
    }

    fibs := make([]int, n+1)
    fibs[0] = 0
    fibs[1] = 1

    for i := 2; i <= n; i++ {
        fibs[i] = fibs[i-1] + fibs[i-2]
    }

    return fibs[n]
}

func main() {
    fmt.Println(Fib(10))
    fmt.Println(Fib(1))
    fmt.Println(Fib(8))
}
```

This program first checks if the input is less than or equal to 1, and if so, it returns the input directly. If the input is greater than 1, it creates an array `fibs` of size `n+1` to store the fibonacci numbers. It initializes the first two elements of `fibs` to 0 and 1 respectively. Then, it computes the fibonacci numbers up to `n` by adding the previous two fibonacci numbers. Finally, it returns the `n`-th fibonacci number from the `fibs` array.

When you run this program, it will output `55`, `1` and `21` as expected.

This solution has a time complexity of O(n) and a space complexity of O(n).

```

```

```python
def Fib(n):
    if n <= 1:
        return n
    else:
        fibs = [0] * (n+1)
        fibs[0] = 0
        fibs[1] = 1
        for i in range(2, n+1):
            fibs[i] = fibs[i-1] + fibs[i