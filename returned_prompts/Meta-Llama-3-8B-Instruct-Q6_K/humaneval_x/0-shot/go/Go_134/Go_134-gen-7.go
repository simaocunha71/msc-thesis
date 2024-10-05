Here is the solution:

```go
import (
    "strings"
)

func CheckIfLastCharIsALetter(txt string) bool {
    // Remove leading and trailing spaces
    txt = strings.TrimSpace(txt)
    
    // Split the string into words
    words := strings.Split(txt, " ")
    
    // Get the last word
    lastWord := words[len(words)-1]
    
    // Check if the last word is not empty
    if lastWord == "" {
        return false
    }
    
    // Check if the last character is an alphabetical character
    if !strings.ContainsAny(lastWord, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return false
    }
    
    // Check if the last character is a part of a word
    if !strings.HasSuffix(lastWord, string(lastWord[len(lastWord)-1])) {
        return false
    }
    
    return true
}
```



Explanation:

1. First, we remove leading and trailing spaces from the input string using `strings.TrimSpace`.
2. Then, we split the string into words using `strings.Split` with a space as the delimiter.
3. We get the last word from the slice of words.
4. We check if the last word is not empty. If it is, we return `false`.
5. We check if the last character of the last word is an alphabetical character using `strings.ContainsAny`. If it is not, we return `false`.
6. Finally, we check if the last character is a part of a word using `strings.HasSuffix`. If it is not, we return `false`.
7. If all the conditions are met, we return `true`. Otherwise, we return `false`.