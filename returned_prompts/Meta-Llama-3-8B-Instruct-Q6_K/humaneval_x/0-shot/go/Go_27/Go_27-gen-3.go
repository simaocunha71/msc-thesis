Here is the solution in Go:

```go
package main

import (
    "strings"
)

// FlipCase flips lowercase characters to uppercase and uppercase to lowercase.
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
    str := "Hello"
    flippedStr := FlipCase(str)
    println(flippedStr)  // Output: hELLO
}
```

This program defines a function called `FlipCase` that takes a string as an argument and returns the flipped string. It iterates over each character in the string, checks if it's lowercase or uppercase using `strings.ToLower` and `strings.ToUpper` functions, and appends the flipped character to the result string. The `main` function demonstrates how to use `FlipCase` with the string "Hello". The output will be "hELLO".