Here is the solution in Go:
```go
package main

import (
    "strings"
)

func CheckIfLastCharIsALetter(txt string) bool {
    // Split the string into words
    words := strings.Split(txt, " ")

    // Check if the last word is not empty
    if len(words) == 0 || words[len(words)-1] == "" {
        return false
    }

    // Check if the last character of the last word is an alphabetical character
    lastWord := words[len(words)-1]
    lastChar := lastWord[len(lastWord)-1]
    if !strings.ContainsRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", lastChar) {
        return false
    }

    // Check if the last character is not part of a word
    if !strings.HasSuffix(lastWord, string(lastChar)) {
        return true
    }

    return false
}

func main() {
    fmt.Println(CheckIfLastCharIsALetter("apple pie"))  // false
    fmt.Println(CheckIfLastCharIsALetter("apple pi e")) // true
    fmt.Println(CheckIfLastCharIsALetter("apple pi e ")) // false
    fmt.Println(CheckIfLastCharIsALetter(""))          // false
}
```
This function first splits the input string into words using the space character as a delimiter. It then checks if the last word is not empty. If it is empty, the function returns false. Otherwise, it checks if the last character of the last word is an alphabetical character using the `strings.ContainsRune` function. If it is not, the function returns false. Finally, it checks if the last character is not part of a word by checking if the last word ends with the last character using the `strings.HasSuffix` function. If it is not part of a word, the function returns true. Otherwise, it returns false.