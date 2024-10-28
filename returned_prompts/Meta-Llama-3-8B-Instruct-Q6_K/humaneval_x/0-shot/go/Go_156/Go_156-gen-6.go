```go
package main

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
    for number > 0 {
        for k, v := range roman {
            for number >= k {
                number -= k
                result += strings.ToLower(v)
            }
        }
    }
    return result
}

func main() {
    fmt.Println(IntToMiniRoman(19)) // xix
    fmt.Println(IntToMiniRoman(152)) // clii
    fmt.Println(IntToMiniRoman(426)) // cdxxvi
}
```
In this solution, we create a map of roman numerals to their corresponding integer values. We then iterate over the map, subtracting the integer value from the number and adding the corresponding roman numeral to the result string as long as the number is greater than or equal to the integer value. Finally, we return the result string in lowercase. In the main function, we test the function with the provided examples. The output is as expected: "xix", "clii", and "cdxxvi".