Here is the solution to the problem:

```go
import (
    "strings"
)

func ReverseDelete(s, c string) [2]interface{} {
    // Convert the string c to a rune slice
    cRunes := []rune(c)
    
    // Create a new string builder to build the result string
    var result strings.Builder
    
    // Iterate over the string s
    for _, runeVal := range []rune(s) {
        // Check if the current rune is in the string c
        found := false
        for _, cRune := range cRunes {
            if runeVal == cRune {
                found = true
                break
            }
        }
        
        // If the rune is not in c, add it to the result string
        if !found {
            result.WriteRune(runeVal)
        }
    }
    
    // Convert the result string to a string
    resultStr := result.String()
    
    // Check if the result string is a palindrome
    isPalindrome := false
    if strings.EqualFold(resultStr, strings.Reverse(resultStr)) {
        isPalindrome = true
    }
    
    // Return the result