The task is to create a function named FlipCase that takes a string as input and returns the string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase.

Here's the solution:
```go
package main

import (
    "strings"
)

func FlipCase(str string) string {
    result := ""
    for _, char := range str {
        if strings.ToLower(string(char)) == string(char) {
            result += strings.ToUpper(string(char))
        } else {
            result += strings.ToLower(string(char))
        }
    }
    return result
}

func main() {
    fmt.Println(FlipCase("Hello"))  // Output: "hELLO"
}
```
In this solution, we iterate over each character in the input string. If the character is lowercase (checked using `strings.ToLower()`), we convert it to uppercase using `strings.ToUpper()` and add it to the result string. If the character is uppercase, we convert it to lowercase using `strings.ToLower()` and add it to the result string. Finally, we return the result string.