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
    roman := ""
    for {
        for key, value := range romanMap {
            if number >= key {
                roman += value
                number -= key
            } else {
                if key == 1 {
                    roman += "i"
                    number -= 1
                }
                break
            }
        }
        if number == 0 {
            break
        }
    }
    return strings.ToLower(roman)
}

func main() {
    fmt.Println(IntToMiniRoman(19)) // xix
    fmt.Println(IntToMiniRoman(152)) // clii
    fmt.Println(IntToMiniRoman(426)) // cdxxvi
}
```



Explanation:

This program uses a map to store the roman numerals and their corresponding integer values. The `IntToMiniRoman` function iterates through the map and appends the roman numeral to the result string if the number is greater than or equal to the value. It then subtracts the value from the number. This process continues until the number becomes 0. The result is then converted to lowercase using the `strings.ToLower` function.

The `main` function demonstrates the usage of the `IntToMiniRoman` function with different inputs. The output is printed to the console.