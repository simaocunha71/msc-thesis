```go
func IntToMiniRoman(number int) string {
    symbols := map[int]string{
        1:    "i",
        4:    "iv",
        5:    "v",
        9:    "ix",
        10:   "x",
        40:   "xl",
        50:   "l",
        90:   "xc",
        100:  "c",
        400:  "cd",
        500:  "d",
        900:  "cm",
        1000: "m",
    }
    result := ""
    for _, v := range []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1} {
        for number >= v {
            result += symbols[v]
            number -= v
        }
    }
    return strings.ToLower(result)
}
```