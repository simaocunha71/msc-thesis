Here is the solution for the problem:

```go
import (
    "strings"
)

func Encrypt(s string) string {
    alphabet := "abcdefghijklmnopqrstuvwxyz"
    encrypted := ""
    for _, char := range s {
        index := strings.Index(alphabet, string(char))
        if index != -1 {
            newIndex := (index + 8) % 26
            encrypted += string(alphabet[newIndex])
        } else {
            encrypted += string(char)
        }
    }
    return encrypted
}
```

In the solution above, we create a string `alphabet` that contains all the letters of the English alphabet. We then loop through each character in the input string `s`. 

For each character, we find its index in the `alphabet` string using the `strings.Index` function. If the character is found in the `alphabet` string, we calculate the new index by adding 8 to the current index and then taking the modulus of 26. This effectively rotates the alphabet by 8 positions. 

We then use the new index to find the corresponding character in the `alphabet` string and add it to the `encrypted` string. If the character is not found in the `alphabet` string, we simply add it to the `encrypted` string without rotating it.

Finally, we return the `encrypted` string.