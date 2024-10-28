Here is the solution in Go:
```go
import (
	"fmt"
)

func DecimalToBinary(decimal int) string {
	binary := fmt.Sprintf("db%bdb", decimal)
	return binary
}

func main() {
	fmt.Println(DecimalToBinary(15))   // returns "db1111db"
	fmt.Println(DecimalToBinary(32))   // returns "db100000db"
}
```
The `DecimalToBinary` function uses the `fmt.Sprintf` function to format the decimal number as a binary string. The `%b` format specifier is used to convert the decimal number to a binary string. The "db" strings are added to the beginning and end of the binary string using the `%b` format specifier.

In the `main` function, we call the `DecimalToBinary` function with the decimal numbers 15 and 32, and print the results. The output will be the expected binary strings with the "db" strings at the beginning and end.