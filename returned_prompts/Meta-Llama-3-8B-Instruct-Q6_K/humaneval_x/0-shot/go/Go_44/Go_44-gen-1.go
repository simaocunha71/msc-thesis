Here is a Go solution for the problem:

```go
import (
    "strconv"
)

func ChangeBase(x int, base int) string {
    var result string
    var temp int
    var digits []rune
    
    for x > 0 {
        temp = x % base
        digits = append(digits, rune(temp+'0'))
        x /= base
    }
    
    for i := len(digits) - 1; i >= 0; i-- {
        result += string(digits[i])
    }
    
    return result
}
```

This function works by repeatedly dividing the input number `x` by the target base, appending the remainder to a slice of runes, and then reversing the slice to form the final string representation of the number in the new base. The function uses the `strconv` package to convert the remainder to a rune (a character) before appending it to the slice, since runes are the Go type for characters. The function returns this final string representation. 

For example, if you call `ChangeBase(8, 3)`, the function will return the string `"22"`, which is the base-3 representation of the number 8. If you call `ChangeBase(8, 2)`, the function will return the string `"1000"`, which is the base-2 representation of the number 8. If you call `ChangeBase(7, 2)`, the function will return the string `"111"`, which is the base-2 representation of the number 7. 

The time complexity of this function is O(log(x)), where x is the input number, since we are repeatedly dividing the input number by the target base until it becomes 0. The space complexity is O(log(x)) as well, since we are storing the digits of the number in a slice. 

Note that this function assumes that the target base is less than 10, as per the problem statement. If you want to handle bases greater than 10, you would need to modify the function to use a different character set, such as uppercase letters or hexadecimal digits. 