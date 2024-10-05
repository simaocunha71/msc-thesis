Here is a simple function in Go that converts a decimal number to a given base (between 2 and 9):

```go
package main

import (
    "fmt"
    "strconv"
)

func ChangeBase(x int, base int) string {
    if base < 2 || base > 9 {
        panic("base must be between 2 and 9")
    }
    digits := []rune{}
    for x > 0 {
        digits = append(digits, rune(x%base+'0'))
        x /= base
    }
    return string(reverse(digits))
}

func reverse(s []rune) []rune {
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        s[i], s[j] = s[j], s[i]
    }
    return s
}

func main() {
    fmt.Println(ChangeBase(8, 3))  // prints "22"
    fmt.Println(ChangeBase(8, 2))  // prints "1000"
    fmt.Println(ChangeBase(7, 2))  // prints "111"
}
```

This function works by repeatedly dividing the input number by the base and appending the remainder to the result. The remainders are converted to characters using the ASCII values of the characters '0' to '9'. The result is then reversed because the digits are appended in reverse order. The function also checks that the base is between 2 and 9. If not, it panics. The main function demonstrates the use of the ChangeBase function.