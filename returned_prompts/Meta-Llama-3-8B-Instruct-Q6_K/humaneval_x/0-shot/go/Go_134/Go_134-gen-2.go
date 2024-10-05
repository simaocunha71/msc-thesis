Here is the solution:
```go
import (
    "strings"
)

func CheckIfLastCharIsALetter(txt string) bool {
    // Remove trailing spaces
    txt = strings.TrimSpace(txt)

    // Check if the string is empty
    if len(txt) == 0 {
        return false
    }

    // Get the last character of the string
    lastChar := txt[len(txt)-1]

    // Check if the last character is an alphabetical character
    if !((lastChar >= 'a' && lastChar <= 'z') || (lastChar >= 'A' && lastChar <= 'Z')) {
        return false
    }

    // Check if the last character is part of a word
    if strings.Index(txt[:len(txt)-1], " ") != -1 {
        return false
    }

    return true
}
```
Explanation:

1. First, we remove trailing spaces from the input string using the `strings.TrimSpace` function.
2. Then, we check if the string is empty. If it is, we return `false`.
3. Next, we get the last character of the string using the `len` function.
4. We check if the last character is an alphabetical character by checking if it is within the range of 'a' to 'z' or 'A' to 'Z'.
5. If the last character is not an alphabetical character, we return `false`.
6. Finally, we check if the last character is part of a word by checking if there is a space character before it using the `strings.Index` function.
7. If the last character is part of a word, we return `false`. Otherwise, we return `true`.

You can test the function with the examples provided to verify that it works correctly.