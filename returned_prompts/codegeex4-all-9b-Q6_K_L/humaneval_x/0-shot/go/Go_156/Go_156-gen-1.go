```go
func IntToMiniRoman(number int) string {
    roman := []string{"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"}
    value := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
    result := ""
    for i, v := range value {
        for number >= v {
            result += roman[i]
            number -= v
        }
    }
    return strings.ToLower(result)
}
```