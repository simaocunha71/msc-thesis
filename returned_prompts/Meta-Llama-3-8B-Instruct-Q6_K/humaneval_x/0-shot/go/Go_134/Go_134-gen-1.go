Here is the solution in Go:
```go
package main

import (
    "strings"
)

func CheckIfLastCharIsALetter(txt string) bool {
    // Split the input string into words
    words := strings.Split(txt, " ")
    
    // If the input string is empty, return false
    if len(words) == 0 {
        return false
    }
    
    // Get the last word
    lastWord := words[len(words)-1]
    
    // If the last word is empty, return false
    if len(lastWord) == 0 {
        return false
    }
    
    // Get the last character of the last word
    lastChar := lastWord[len(lastWord)-1]
    
    // Check if the last character is an alphabetical character
    if !((lastChar >= 'a' && lastChar <= 'z') || (lastChar >= 'A' && lastChar <= 'Z')) {
        return false
    }
    
    // Check if the last character is not part of a word
    if len(lastWord) > 1 {
        return false
    }
    
    // If all conditions are met, return true
    return true
}

func main() {
    fmt.Println(CheckIfLastCharIsALetter("apple pie"))  // false
    fmt.Println(CheckIfLastCharIsALetter("apple pi e")) // true
    fmt.Println(CheckIfLastCharIsALetter("apple pi e ")) // false
    fmt.Println(CheckIfLastCharIsALetter(""))            // false
}
```
This function works by first splitting the input string into words using the `strings.Split` function. It then checks if the last word is empty, and if so, returns `false`. It then gets the last character of the last word and checks if it is an alphabetical character using a simple ASCII range check. Finally, it checks if the last character is not part of a word by checking if the last word has more than one character. If all conditions are met, the function returns `true`. Otherwise, it returns `false`. The `main` function demonstrates the usage of the `CheckIfLastCharIsALetter` function with different inputs.