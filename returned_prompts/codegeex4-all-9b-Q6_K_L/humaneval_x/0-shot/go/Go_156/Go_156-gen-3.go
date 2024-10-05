```go
func IntToMiniRoman(number int) string {
    roman := []string{"i", "iv", "v", "ix", "x", "xl", "l", "xc", "c", "cd", "d", "cm", "m"}
    val := []int{1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000}
    result := ""
    for i := len(roman) - 1; i >= 0; i-- {
        for number >= val[i] {
            result += roman[i]
            number -= val[i]
        }
    }
    return strings.ToLower(result)
}
```
