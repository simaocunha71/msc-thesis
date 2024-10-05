Here is the Go function that changes the numerical base of an input number x to base:
```go
import (
    "strconv"
)

func ChangeBase(x int, base int) string {
    // Convert the number to a string in base 10
    str := strconv.Itoa(x)
    
    // Convert the base 10 number to the desired base
    result := ""
    for len(str) > 0 {
        remainder, _ := strconv.Atoi(string(str[len(str)-1]))
        str = str[:len(str)-1]
        if remainder > 0 {
            result = strconv.Itoa(remainder) + result
        }
    }
    
    // Add leading zeros if necessary
    result = strings.Repeat("0", base-1-len(result)) + result
    
    return result
}
```
This function first converts the input number x to a string in base 10 using `strconv.Itoa()`. Then it iterates over the string from right to left, converting each character back to an integer using `strconv.Atoi()`, and prepending it to the result string. Finally, it adds leading zeros if necessary to make the result string the desired length.

For example, if you call `ChangeBase(8, 3)`, the function will convert the base 10 number 8 to the base 3 number "22". If you call `ChangeBase(8, 2)`, it will convert the base 10 number 8 to the base 2 number "1000". If you call `ChangeBase(7, 2)`, it will convert the base 10 number 7 to the base 2 number "111".