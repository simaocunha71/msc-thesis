```go
func IntToMiniRoman(number int) string {
    roman := []string{"i", "iv", "v", "ix", "x", "xl", "l", "xc", "c", "cd", "d", "cm", "m"}
    arab := []int{1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000}
    result := ""
    for i := len(roman) - 1; i >= 0; i-- {
        for number >= arab[i] {
            result += roman[i]
            number -= arab[i]
        }
    }
    return strings.ToLower(result)
}
```
