
```
func CircularShift(x int,shift int) string {
    s := strconv.Itoa(x)
    l := len(s)
    if shift > l {
        shift = shift % l
    }
    return s[shift:] + s[:shift]
}
```

Explanation:

The CircularShift function takes an integer x and an integer shift as parameters. It converts the integer x into a string using strconv.Itoa function and stores it in the variable s. Then, it calculates the length of the string s and stores it in the variable l. 

Next, it checks if the shift value is greater than the length of the string. If it is, it means that the shift value is greater than the number of digits in the integer. In this case, it calculates the modulus of the shift value with the length of the string and assigns it back to the shift variable. This ensures that the shift value is within the range of the number of digits in the integer.

Finally, it returns the result of slicing the string s starting from the shift index till the end, concatenated with the slicing of the string s starting from the beginning till the shift index. This effectively circularly shifts the digits of the integer x to the right by the specified shift value.

The provided code is an implementation of the CircularShift function in Go programming language.

To test the CircularShift function, you can use the following test cases:

```go
package main

import (
    "fmt"
    "strconv"
)

func CircularShift(x int, shift int) string {
    s := strconv.Itoa(x)
    l := len(s)
    if shift > l {
        shift = shift % l
    }
    return s[shift:] + s[:shift]
}

func main() {
    fmt.Println(CircularShift(12, 1))  // "21"
    fmt.Println(CircularShift(12, 2))  // "12"
}
```

When you run the above code, it will output the following:

```
21
12
``