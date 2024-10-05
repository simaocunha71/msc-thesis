Here is the solution to the problem:

```go
import (
    "strings"
)

// Given a positive integer, obtain its roman numeral equivalent as a string,
// and return it in lowercase.
// Restrictions: 1 <= num <= 1000
// 
// Examples:
// >>> IntToMiniRoman(19) == 'xix'
// >>> IntToMiniRoman(152) == 'clii'
// >>> IntToMiniRoman(426) == 'cdxxvi'
func IntToMiniRoman(number int) string {
    romanMap := map[int]string{
        1: "i",
        4: "iv",
        5: "v",
        9: "ix",
        10: "x",
        40: "xl",
        50: "l",
        90: "xc",
        100: "c",
        400: "cd",
        500: "d",
        900: "cm",
        1000: "m",
    }
    result := ""
    for key, value := range romanMap {
        while number >= key {
            result += value
            number -= key
        }
    }
    return strings.ToLower(result)
}
```

This function works by iterating over the Roman numeral map in descending order, subtracting the value from the number as many times as possible, and appending the corresponding Roman numeral to the result string. The `strings.ToLower` function is used to convert the result to lowercase. The function returns the Roman numeral equivalent of the given number as a string.