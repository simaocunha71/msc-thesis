Here is a possible solution in Go:
```go
package main

import (
    "strings"
)

func CheckIfLastCharIsALetter(txt string) bool {
    // Split the string into words
    words := strings.Split(txt, " ")

    // Get the last word
    lastWord := words[len(words)-1]

    // Check if the last word is not empty
    if len(lastWord) == 0 {
        return false
    }

    // Check if the last character of the last word is an alphabetical character
    lastChar := lastWord[len(lastWord)-1]
    if !strings.ContainsAny(string(lastChar), "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return false
    }

    // Check if the last character is not part of a word
    if !strings.Contains(txt, lastChar) {
        return true
    }

    return false
}

func main() {
    fmt.Println(CheckIfLastCharIsALetter("apple pie")) // false
    fmt.Println(CheckIfLastCharIsALetter("apple pi e")) // true
    fmt.Println(CheckIfLastCharIsALetter("apple pi e ")) // false
    fmt.Println(CheckIfLastCharIsALetter("")) // false
}
```
This function splits the input string into words using the `strings.Split` function. Then it gets the last word and checks if it's not empty. If it's not empty, it checks if the last character is an alphabetical character using the `strings.ContainsAny` function. If it is, it checks if the last character is not part of a word by checking if it's present in the original string using the `strings.Contains` function. If it's not part of a word, the function returns `true`. Otherwise, it returns `false`.