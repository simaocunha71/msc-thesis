```go
import (
	"strconv"
)

func Digits(n int) int {
    product := 1
    hasOdd := false
    for _, digit := range strconv.Itoa(n) {
        intDigit, _ := strconv.Atoi(string(digit))
        if intDigit%2 != 0 {
            product *= intDigit
            hasOdd = true
        }
    }
    if !hasOdd {
        return 0
    }
    return product
}
```
