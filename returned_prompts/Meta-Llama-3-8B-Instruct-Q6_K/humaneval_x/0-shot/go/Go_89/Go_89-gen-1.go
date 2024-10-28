Here is the solution:

```go
import (
    "strings"
)

func Encrypt(s string) string {
    alphabet := "abcdefghijklmnopqrstuvwxyz"
    result := ""
    for _, c := range s {
        if strings.ToLower(string(c)) >= alphabet[0] && strings.ToLower(string(c)) <= alphabet[len(alphabet)-1] {
            index := strings.Index(alphabet, strings.ToLower(string(c)))
            result += string(alphabet[(index+2*2)%len(alphabet)] + 97)
        } else {
            result += string(c)
        }
    }
    return result
}
```
This function works by iterating over each character in the input string. If the character is a lowercase letter, it finds the index of the character in the alphabet, shifts it down by 4 places (2*2), and adds it to the result string. If the character is not a letter, it simply adds it to the result string. The `strings.ToLower` function is used to ensure the function works correctly for both lowercase and uppercase letters. The `%len(alphabet)` is used to wrap around the alphabet if the shifted index is out of range. The `97` is used to convert the ASCII value of the character back to a lowercase letter. The function then returns the encrypted string. 