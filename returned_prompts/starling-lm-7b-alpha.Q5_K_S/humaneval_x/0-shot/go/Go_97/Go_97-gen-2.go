    return (a%10)*(b%10)





































































```
```

```

```

```

```
```

```

```

```
```
```

Answer:

In order to solve this problem, we can follow these steps:

1. Use the modulo operator `%` to get the remainder of `a` divided by 10, and assign it to variable `aUnit`.
2. Use the modulo operator `%` to get the remainder of `b` divided by 10, and assign it to variable `bUnit`.
3. Multiply `aUnit` and `bUnit` together and return the result.

Here's the code that implements this solution:

```go
func Multiply(a, b int) int {
    aUnit := a % 10
    bUnit := b % 10
    return aUnit * bUnit
}
```

This function takes two integers `a` and `b` as input, and returns the product of their unit digits. For example, if we call `Multiply(148, 412)`, the function will return 16, as the unit digit of 148 is 8 and the unit digit of 412 is 2, and 8 * 2 is 16.

You can use this function to solve the problem and get the desired result.

```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println(Multiply(148, 412))   // Output: 16
    fmt.Println(Multiply(19, 28))      // Output: 72
    fmt.Println(Multiply(2020, 1851))  // Output: