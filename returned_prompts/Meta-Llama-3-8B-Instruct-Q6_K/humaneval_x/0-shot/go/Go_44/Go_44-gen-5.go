Here is a simple and efficient solution in Go:

```go
import (
    "strconv"
)

func ChangeBase(x int, base int) string {
    if x == 0 {
        return "0"
    }
    if base < 2 || base > 9 {
        panic("base must be between 2 and 9")
    }
    digits := []byte{}
    for x > 0 {
        digits = []byte(strconv.Itoa(x % base)) + digits
        x /= base
    }
    return string(digits)
}
```

This function works by repeatedly dividing the input number `x` by the target base and appending the remainder to the result. The result is a string representation of the number in the target base. The function also includes some basic error checking to ensure that the target base is within the valid range of 2 to 9. If the target base is outside this range, the function will panic. 

This solution is efficient because it uses a single loop to convert the number and it uses the built-in `strconv.Itoa` function to convert the remainder to a string, which is efficient. The time complexity of this solution is O(log(x)), where x is the input number. The space complexity is O(log(x)) as well, because we need to store the result string. 

You can test this function with the examples you provided:

```go
fmt.Println(ChangeBase(8, 3))  // Output: "22"
fmt.Println(ChangeBase(8, 2))  // Output: "1000"
fmt.Println(ChangeBase(7, 2))  // Output: "111"
``` 

Note: The `strconv.Itoa` function is used to convert an integer to a string. It returns a string representation of the integer. The `[]byte` type is used to create a byte slice from the string. The `+` operator is used to concatenate the byte slices. The `string` function is used to convert the byte slice back to a string. 