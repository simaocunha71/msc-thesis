You can convert the integer into its binary representation and then sum up the digits. Here is a solution in Go:

```go
import (
	"fmt"
	"strconv"
)

func Solve(N int) string {
	binary := strconv.FormatInt(int64(N), 2)
	sum := 0
	for _, c := range binary {
		digit, _ := strconv.Atoi(string(c))
		sum += digit
	}
	return strconv.Itoa(sum)
}
```

This code first converts the integer `N` into a binary string using `strconv.FormatInt`. Then it iterates over each character in the string and converts it to a digit using `strconv.Atoi`. It adds up all the digits and returns the sum as a string.

For example, if `N` is 147, `strconv.FormatInt(int64(N), 2)` returns "1100". The for loop then converts each character to a digit and adds them up, resulting in 12. Finally, `strconv.Itoa(sum)` returns the sum as a string.