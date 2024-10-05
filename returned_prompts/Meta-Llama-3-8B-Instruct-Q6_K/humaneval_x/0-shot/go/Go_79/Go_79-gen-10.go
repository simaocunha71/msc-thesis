Here is a simple solution in Go:
```go
import (
	"fmt"
)

func DecimalToBinary(decimal int) string {
	return "db" + fmt.Sprintf("%b", decimal) + "db"
}
```
Explanation:

* The `fmt.Sprintf` function is used to convert the decimal number to a binary string. The `%b` format specifier is used to format the number as a binary string.
* The `DecimalToBinary` function returns a string that starts with "db", followed by the binary representation of the decimal number, and ends with "db". This satisfies the problem requirements.

You can test this function with the examples provided:
```go
fmt.Println(DecimalToBinary(15))  // Output: db1111db
fmt.Println(DecimalToBinary(32))  // Output: db100000db
```
This solution is concise and easy to understand. It uses the built-in `fmt.Sprintf` function to convert the decimal number to a binary string, and then concatenates the extra characters "db" to the beginning and end of the string.