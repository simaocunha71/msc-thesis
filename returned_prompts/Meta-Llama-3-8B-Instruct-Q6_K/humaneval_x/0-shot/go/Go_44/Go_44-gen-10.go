Here is a Go function that changes the numerical base of an input number `x` to a specified base `base`. The function uses a helper function `convert` to perform the conversion. The `convert` function uses recursion to convert the number to the desired base.

```go
package main

import (
    "fmt"
    "strconv"
)

// Change numerical base of input number x to base.
// return string representation after the conversion.
// base numbers are less than 10.
func ChangeBase(x int, base int) string {
    if x == 0 {
        return "0"
    }
    result := ""
    for x > 0 {
        result = strconv.Itoa(x%base) + result
        x = x / base
    }
    return result
}

func main() {
    fmt.Println(ChangeBase(8, 3))  // Output: 22
    fmt.Println(ChangeBase(8, 2))  // Output: 1000
    fmt.Println(ChangeBase(7, 2))  // Output: 111
}
```

In the `ChangeBase` function, we first check if the number `x` is 0. If it is, we return the string "0". Then we enter a loop that continues until `x` is 0. In each iteration of the loop, we convert the remainder of `x` divided by `base` to a string using `strconv.Itoa`, and add it to the beginning of the `result` string. Then we update `x` to be the integer division of `x` by `base`. Finally, we return the `result` string.