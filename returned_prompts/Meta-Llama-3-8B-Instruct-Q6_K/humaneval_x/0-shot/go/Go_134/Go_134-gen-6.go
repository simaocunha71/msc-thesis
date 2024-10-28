Here is a possible solution:
```go
import (
    "strings"
)

func CheckIfLastCharIsALetter(txt string) bool {
    // Remove trailing spaces
    txt = strings.TrimSpace(txt)
    // Check if the last character is an alphabetical character
    if !strings.ContainsAny(txt, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return false
    }
    // Check if the last character is part of a word
    if len(txt) > 1 && txt[len(txt)-2] == ' ' {
        return false
    }
    return true
}
```
Here's an explanation of the solution:

1. We use the `strings.TrimSpace` function to remove any trailing spaces from the input string.
2. We check if the last character of the string is an alphabetical character using the `strings.ContainsAny` function. If it's not, we return `false`.
3. We check if the last character is part of a word by checking if the character before it is a space. If it is, we return `false`.

With these checks, the function should return `true` if the last character of the input string is an alphabetical character and is not part of a word, and `false` otherwise.