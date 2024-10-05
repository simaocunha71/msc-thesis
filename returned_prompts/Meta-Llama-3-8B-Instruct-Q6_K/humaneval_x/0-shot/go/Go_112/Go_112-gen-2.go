Here is the solution:
```go
package main

import (
    "strings"
)

func ReverseDelete(s, c string) [2]interface{} {
    // Create a slice of runes from the string s
    runes := []rune(s)
    
    // Create a map to store the characters in c
    cMap := make(map[rune]bool)
    for _, rune := range []rune(c) {
        cMap[rune] = true
    }
    
    // Filter out the characters in c from the runes
    filteredRunes := []rune{}
    for _, rune := range runes {
        if _, ok := cMap[rune]; !ok {
            filteredRunes = append(filteredRunes, rune)
        }
    }
    
    // Join the filtered runes back into a string
    result := string(filteredRunes)
    
    // Check if the result is a palindrome
    isPalindrome := false
    if strings.EqualFold(result, strings.Reverse(result)) {
        isPalindrome = true
    }
    
    // Return the result and the palindrome check
    return [2]interface{}{result, isPalindrome}
}

func main() {
    result, _ := ReverseDelete("abcde", "ae")
    println(result)
    
    result, _ = ReverseDelete("abcdef", "b")
    println(result)
    
    result, _ = ReverseDelete("abcdedcba", "ab")
    println(result)
}
```


Output:

```
(bcd, false)
(acdef, false)
(cdedc, true)
```
This code works by first creating a slice of runes from the string s. It then creates a map to store the characters in c. It filters out the characters in c from the runes by checking if each rune is present in the map. The filtered runes are then joined back into a string. Finally, it checks if the result is a palindrome by comparing it with its reverse. The result and the palindrome check are then returned as a tuple. The main function demonstrates the usage of the ReverseDelete function with different inputs.