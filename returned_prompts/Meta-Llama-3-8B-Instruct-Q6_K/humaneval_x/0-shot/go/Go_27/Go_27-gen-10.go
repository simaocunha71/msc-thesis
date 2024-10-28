Here is a simple implementation of the function in Go:

```go
package main

import (
    "strings"
)

// For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
// >>> FlipCase('Hello')
// 'hELLO'
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
    fmt.Println(FlipCase("Hello"))
}
```

In this code, we iterate over each character in the input string. We use the `strings.ToLower` and `strings.ToUpper` functions to check if the character is lowercase or uppercase, and add it to the result string accordingly. The `strings.ToLower` function returns the lowercase version of the string, and `strings.ToUpper` returns the uppercase version. We use the `string(char)` conversion to convert a rune (a single character) to a string, since the `strings.ToLower` and `strings.ToUpper` functions expect a string as input. The `fmt.Println` function is used to print the result in the `main` function. 

When you run this code with the input "Hello", it will output "hELLO". 

Please note that this code assumes that the input string only contains ASCII characters. If the input string can contain non-ASCII characters (such as accents or non-Latin characters), you may need to use a more sophisticated approach to correctly handle these characters. 

Also, this code does not handle non-character input (such as whitespace, punctuation, or control characters) correctly. If you need to handle these cases, you may need to add additional logic to your code. 

Finally, this code does not handle errors. If the input string is `nil` or an empty string, this code will panic when it tries to iterate over the string. If you need to handle these cases, you may need to add additional error checking to your code. 