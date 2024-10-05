Here is the solution in Go programming language:

```go
package main

import (
    "strings"
)

// For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
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
    fmt.Println(FlipCase(str))  // Output: "hELLO"
}
```

Explanation:

1.  We create a new empty string `result` to store the modified characters.
2.  We loop through each character in the input string `str` using a range-based loop.
3.  For each character, we check if it's a lowercase character by converting it to lowercase using `strings.ToLower` and comparing it with the original character. If they're equal, it means the character is lowercase.
4.  If the character is lowercase, we convert it to uppercase using `strings.ToUpper` and add it to the `result` string. If it's uppercase, we convert it to lowercase using `strings.ToLower` and add it to the `result` string.
5.  Finally, we return the modified `result` string.

In the `main` function, we test the `FlipCase` function with the input string `"Hello"` and print the output, which is `"hELLO"`. This demonstrates the flipping of lowercase characters to uppercase and uppercase characters to lowercase.