Here is the solution in Go:
```go
package main

import (
    "fmt"
    "strings"
)

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
    for num, roman := range romanMap {
        for number >= num {
            result += roman
            number -= num
        }
    }
    return strings.ToLower(result)
}

func main() {
    fmt.Println(IntToMiniRoman(19)) // xix
    fmt.Println(IntToMiniRoman(152)) // clii
    fmt.Println(IntToMiniRoman(426)) // cdxxvi
}
```
This code uses a map to store the roman numerals and their corresponding values. It then iterates over the map, subtracting the values from the input number and appending the corresponding roman numerals to the result string. Finally, it converts the result to lowercase using the `strings.ToLower` function. The `main` function tests the `IntToMiniRoman` function with the provided examples.