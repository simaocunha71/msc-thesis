Here is a simple implementation of the function ChangeBase in Go. This function converts an integer to a specified base and returns the result as a string.

```go
package main

import (
    "strconv"
    "fmt"
)

// Change numerical base of input number x to base.
// return string representation after the conversion.
// base numbers are less than 10.
func ChangeBase(x int, base int) string {
    // Convert the integer to a string in the specified base
    str := strconv.FormatInt(int64(x), base)
    // Convert the string to uppercase
    for i := 0; i < len(str); i++ {
        c := str[i]
        if c >= 'a' && c <= 'z' {
            str[i] = 'A' + c - 'a'
        }
    }
    return str
}

func main() {
    fmt.Println(ChangeBase(8, 3))  // Output: 22
    fmt.Println(ChangeBase(8, 2))  // Output: 1000
    fmt.Println(ChangeBase(7, 2))  // Output: 111
}
```

In this code, we use the `strconv.FormatInt` function to convert the integer `x` to a string in the specified base. Then we convert the string to uppercase by iterating over the characters in the string and replacing any lowercase letters with their uppercase counterparts. The result is the string representation of the integer in the specified base. 

The `main` function demonstrates how to use the `ChangeBase` function with different inputs. The output of each call to `ChangeBase` is printed to the console. 

This code assumes that the base is less than 10, as specified in the problem description. If the base can be greater than 10, the code would need to be modified to handle this case. 

Note that this code does not handle the case where the base is 1. In this case, the result would be a string of spaces, which is not a valid representation of a number in any base. If you need to handle this case, you would need to add additional code to handle the conversion of the integer to a string in base 1. 

This code also assumes that the input integer is non-negative. If you need to handle negative integers, you would need to add additional code to handle the sign of the integer. 

This code does not handle the case where the base is greater than 36