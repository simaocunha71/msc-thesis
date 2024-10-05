Here is the solution using a map to store the roman numerals and their corresponding integer values:

```go
import (
    "fmt"
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
        900:  "cm",
        500:  "d",
        400:  "cd",
        100:  "c",
        90:   "xc",
        50:   "l",
        40:   "xl",
        10:   "x",
        9:    "ix",
        5:    "v",
        4:    "iv",
        1:    "i",
    }

    result := ""
    for value, roman := range romanMap {
        for number >= value {
            result += roman
            number -= value
        }
    }
    return strings.ToLower(result)
}

func main() {
    fmt.Println(IntToMiniRoman(19))  // Output: xix
    fmt.Println(IntToMiniRoman(152)) // Output: clii
    fmt.Println(IntToMiniRoman(426)) // Output: cdxxvi
}
```
This function works by iterating over the romanMap in descending order of value. For each value, it appends the corresponding roman numeral to the result string as many times as possible without exceeding the given number. Finally, it returns the result string in lowercase. The main function is used to test the IntToMiniRoman function with the given examples. The output will be the roman numeral equivalent of the given numbers in lowercase.