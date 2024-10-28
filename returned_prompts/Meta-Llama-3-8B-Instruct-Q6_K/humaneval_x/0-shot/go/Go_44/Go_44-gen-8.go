Here is the solution in Go:
```go
package main

import (
    "fmt"
    "strconv"
)

func ChangeBase(x int, base int) string {
    if x == 0 {
        return "0"
    }
    digits := []rune{}
    for x > 0 {
        digits = []rune{[]rune("0123456789")[x%base]} + digits
        x /= base
    }
    return string(digits)
}

func main() {
    fmt.Println(ChangeBase(8, 3))  // Output: 22
    fmt.Println(ChangeBase(8, 2))  // Output: 1000
    fmt.Println(ChangeBase(7, 2))  // Output: 111
}
```

Explanation:

*   We use the modulo operator `%` to get the remainder of `x` divided by `base`. This gives us the next digit of the output.
*   We use integer division `/` to divide `x` by `base` and move to the next iteration.
*   We concatenate the new digit to the beginning of the `digits` slice, which will contain the digits of the output number in reverse order.
*   When `x` becomes 0, we have processed all the digits, and the `digits` slice contains the output number in the desired base.
*   We convert the `digits` slice to a string using the `string()` function and return it.

This function works for bases less than 10, as required. For larger bases, you would need to modify the function to handle the extra digits.