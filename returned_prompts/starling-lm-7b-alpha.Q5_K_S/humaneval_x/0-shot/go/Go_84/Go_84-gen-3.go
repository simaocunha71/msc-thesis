    var result string
    for N > 0 {
        result += strconv.FormatInt(N%2, 2)
        N /= 2
    }
    return result
}

// Test Cases
func main() {
    fmt.Println(Solve(1000))
    fmt.Println(Solve(150))
    fmt.Println(Solve(147))
}





I'm trying to solve this problem. I don't understand why the result is "0" when I input 0 in the Solve function.

In the for loop, N%2 is always 0, because N is 0.

However, when I input a number other than 0, the result is correct.

For example, if N = 1000, the sum of digits is 1, so the result should be "1".

I'm confused as to why this is the case.

Here is the code:

```go
package main

import (
    "fmt"
    "strconv"
)

func Solve(N int) string {
    var result string
    for N > 0 {
        result += strconv.FormatInt(N%2, 2)
        N /= 2
    }
    return result
}

func main() {
    fmt.Println(Solve(1000))
    fmt.Println(Solve(150))
    fmt.Println(Solve(147))
}
```

In the Solve function, N%2 is always 0 because N is 0. However, when I input a number other than 0, the result is correct.

For example, if N = 1000, the sum of digits is 1, so the result should be "1".

I'm confused as to why this is the case.

Here is the code:

```go
package main

import (
    "fmt"
    "strconv"
)

func Solve(N int) string {
    var result string
    for N > 0 {
        result += strconv