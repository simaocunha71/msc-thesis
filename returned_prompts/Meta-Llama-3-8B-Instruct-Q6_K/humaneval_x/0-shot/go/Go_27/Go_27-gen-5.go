Here is a simple and efficient solution using the `strings` package in Go. This function uses a loop to iterate over each character in the input string, and checks if the character is lowercase or uppercase. If it's lowercase, it converts it to uppercase using the `unicode.ToUpper` function, and if it's uppercase, it converts it to lowercase using the `unicode.ToLower` function.

```go
import (
    "strings"
    "unicode"
)

func FlipCase(str string) string {
    var result strings.Builder
    for _, char := range str {
        if unicode.IsLower(char) {
            result.WriteByte(unicode.ToUpper(char)[0])
        } else {
            result.WriteByte(unicode.ToLower(char)[0])
        }
    }
    return result.String()
}
```

This function uses a `strings.Builder` to efficiently build the resulting string. It loops over each character in the input string, checks if it's lowercase or uppercase, and appends the converted character to the result string. The `unicode.IsLower` and `unicode.IsUpper` functions are used to check if a character is lowercase or uppercase, respectively. The `unicode.ToUpper` and `unicode.ToLower` functions are used to convert characters to uppercase and lowercase, respectively. The `[0]` index is used to get the byte value of the character. The `result.String()` function is used to get the final resulting string.