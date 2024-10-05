Here is a Go solution for the problem:

```go
import (
    "strings"
)

func IntToMiniRoman(number int) string {
    val := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
    syb := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
    roman := ""
    i := 0
    for number > 0 {
        for number >= val[i] {
            number -= val[i]
            roman += syb[i]
        }
        i++
    }
    return strings.ToLower(roman)
}
```

This function works by iterating over the list of roman numeral values and symbols. For each value, it subtracts the value from the number as many times as it can, and appends the corresponding symbol to the roman string. This process continues until the number becomes 0. Finally, it returns the roman string in lowercase using the `strings.ToLower` function.