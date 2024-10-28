Here is a simple and efficient solution in Go:

```go
import (
	"fmt"
)

func DecimalToBinary(decimal int) string {
	binary := ""
	for decimal > 0 {
		remainder := decimal % 2
		if remainder == 1 {
			binary = "1" + binary
		} else {
			binary = "0" + binary
		}
		decimal = decimal / 2
	}
	return "db" + binary + "db"
}

func main() {
	fmt.Println(DecimalToBinary(15))  // Output: db1111db
	fmt.Println(DecimalToBinary(32))  // Output: db100000db
}
```

This function works by repeatedly dividing the input decimal number by 2 and appending the remainder (which will be either 0 or 1) to the front of the binary string. This process is repeated until the decimal number becomes 0. The resulting binary string is then prepended with "db" and appended with "db". This ensures that the output meets the requirements of having "db" at the beginning and at the end. The main function demonstrates this by calling the DecimalToBinary function with the inputs 15 and 32. The output for these inputs is "db1111db" and "db100000db", respectively. 