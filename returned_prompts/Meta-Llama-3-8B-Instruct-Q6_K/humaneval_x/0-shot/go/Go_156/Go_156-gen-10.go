Here is the solution:

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
        1000: "m",
        900: "cm",
        500: "d",
        400: "cd",
        100: "c",
        90: "xc",
        50: "l",
        40: "xl",
        10: "x",
        9: "ix",
        5: "v",
        4: "iv",
        1: "i",
    }
    result := ""
    for k, v := range romanMap {
        for number >= k {
            result += v
            number -= k
        }
    }
    return strings.ToLower(result)
}
```



Explanation:

The solution uses a map to store the roman numerals and their corresponding integer values. It then iterates through the map and appends the roman numerals to the result string as long as the number is greater than or equal to the integer value. The number is then decremented by the integer value. Finally, the result string is converted to lowercase using the strings.ToLower function.