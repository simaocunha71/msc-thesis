To convert a decimal number to binary in Go, you can use the `strconv` package's `FormatInt` function. This function takes two arguments: the integer to convert and the base for the conversion (in this case, 2 for binary). Here's how you can implement the `DecimalToBinary` function:

```go
package main

import (
	"fmt"
	"strconv"
)

// You will be given a number in decimal form and your task is to convert it to
// binary format. The function should return a string, with each character representing a binary
// number. Each character in the string will be '0' or '1'.
//
// There will be an extra couple of characters 'db' at the beginning and at the end of the string.
// The extra characters are there to help with the format.
//
// Examples:
// DecimalToBinary(15)   # returns "db1111db"
// DecimalToBinary(32)   # returns "db100000db"
func DecimalToBinary(decimal int) string {
	return "db" + strconv.FormatInt(int64(decimal), 2) + "db"
}

func main() {
	fmt.Println(DecimalToBinary(15))   // returns "db1111db"
	fmt.Println(DecimalToBinary(32))   // returns "db100000db"
}
```

In this code, `strconv.FormatInt(int64(decimal), 2)` converts the decimal number to binary and returns it as a string. We then prepend and append "db" to the binary string to match the expected format.

You can test this function with the given examples to ensure it works correctly.