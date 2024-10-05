```go
func IntToMiniRoman(number int) string {
    romanNumerals := []string{"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"}
    values := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
    result := ""
    for i, val := range values {
        for number >= val {
            result += romanNumerals[i]
            number -= val
        }
    }
    return strings.ToLower(result)
}
```
