Here is a simple function in Go that converts an integer to its Roman numeral equivalent:

```go
import (
    "strings"
)

func IntToMiniRoman(number int) string {
    roman := make(map[int]string)
    roman[1] = "i"
    roman[4] = "iv"
    roman[5] = "v"
    roman[9] = "ix"
    roman[10] = "x"
    roman[40] = "xl"
    roman[50] = "l"
    roman[90] = "xc"
    roman[100] = "c"
    roman[400] = "cd"
    roman[500] = "d"
    roman[900] = "cm"
    roman[1000] = "m"

    result := ""
    for _, value := range []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1} {
        for number >= value {
            result += roman[value]
            number -= value
        }
    }
    return strings.ToLower(result)
}
```
This function works by first creating a map of Roman numerals and their corresponding integer values. It then iterates over a list of integer values in descending order, subtracting the largest possible value from the input number and appending the corresponding Roman numeral to the result string. This process is repeated until the input number is reduced to 0. Finally, the result string is converted to lowercase and returned.