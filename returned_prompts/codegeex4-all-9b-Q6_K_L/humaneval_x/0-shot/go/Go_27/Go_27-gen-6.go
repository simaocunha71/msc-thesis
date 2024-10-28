You can accomplish this task by utilizing the `strings.ToLower()` and `strings.ToUpper()` functions in Go. Here is the solution:

```go
import (
    "strings"
)

func FlipCase(str string) string {
    for i, r := range str {
        if r >= 'a' && r <= 'z' {
            str = strings.Replace(str, string(r), strings.ToUpper(string(r)), 1)
        } else if r >= 'A' && r <= 'Z' {
            str = strings.Replace(str, string(r), strings.ToLower(string(r)), 1)
        }
    }
    return str
}
```
This solution iterates over each character in the string. If the character is lowercase, it replaces it with the same character, but in uppercase. If the character is uppercase, it replaces it with the same character, but in lowercase. The `strings.Replace()` function is used for this purpose. This function replaces the first occurrence of a substring with a new substring, and it returns the modified string.