Here is the solution:

```go
import (
	"fmt"
)

func DecimalToBinary(decimal int) string {
	binary := fmt.Sprintf("%b", decimal)
	return "db" + strings.Repeat("0", len(binary)) + binary + strings.Repeat("0", len(binary)) + "db"
}
```

Explanation:
The `DecimalToBinary` function takes an integer `decimal` as input and returns a string. It uses the `fmt.Sprintf` function to convert the decimal number to binary format using the `%b` format specifier. The `strings.Repeat` function is used to add leading zeros to the binary string to make its length even. Finally, the function returns the resulting string with the extra "db" characters added at the beginning and end.