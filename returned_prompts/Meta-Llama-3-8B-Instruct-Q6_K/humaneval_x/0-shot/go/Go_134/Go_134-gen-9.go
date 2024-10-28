Here is the solution in Go:

```go
import (
    "strings"
)

func CheckIfLastCharIsALetter(txt string) bool {
    // Split the string into words
    words := strings.Split(txt, " ")

    // Check if the last word is empty
    if len(words) == 0 {
        return false
    }

    // Get the last word
    lastWord := words[len(words)-1]

    // Check if the last character of the last word is an alphabetical character
    if strings.ContainsAny(lastWord, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        // Check if the last word is the last word of the string
        if len(txt) == len(lastWord) {
            return false
        } else {
            // Check if the last character of the string is a space
            if txt[len(txt)-1] == ' ' {
                return false
            } else {
                return true
            }
        }
    } else {
        return false
    }
}
```


This function splits the input string into words, then checks the last word. If the last word is not empty, it checks if the last character of the last word is an alphabetical character. If it is, it checks if the last word is the last word of the string, and if it's not, it checks if the last character of the string is a space. If any of these conditions are not met, it returns false. Otherwise, it returns true.