Here is a possible implementation of the `IntToMiniRoman` function in Go:
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
    fmt.Println(IntToMiniRoman(19))  // Output: "xix"
    fmt.Println(IntToMiniRoman(152)) // Output: "clii"
    fmt.Println(IntToMiniRoman(426)) // Output: "cdxxvi"
}
```
This implementation uses a map to store the roman numeral values and their corresponding decimal values. It then iterates over the map and appends the roman numeral values to the result string until the input number is reduced to 0. Finally, it returns the result string in lowercase using the `strings.ToLower` function.

The `main` function demonstrates the usage of the `IntToMiniRoman` function with the examples provided. You can run this code and verify the output to see that it matches the expected results.