Here is a Go function that accomplishes the task:

```go
import (
    "strings"
)

func ReverseDelete(s, c string) [2]interface{} {
    // Create a set of characters to delete
    toDelete := make(map[rune]bool)
    for _, char := range c {
        toDelete[rune(char)] = true
    }

    // Create a new string with characters not in the set
    result := ""
    for _, char := range s {
        if !toDelete[rune(char)] {
            result += string(char)
        }
    }

    // Check if the result string is a palindrome
    isPalindrome := true
    for i := 0; i < len(result)/2; i++ {
        if result[i] != result[len(result)-1-i] {
            isPalindrome = false
            break
        }
    }

    // Return the result string and a boolean indicating if it's a palindrome
    return [2]interface{}{result, isPalindrome}
}
```

This function works by creating a set of characters to delete from the string `c`. Then it iterates over the string `s` and adds characters that are not in the set to the result string. Finally, it checks if the result string is a palindrome by comparing characters from the start and end of the string, moving towards the center. If any pair of characters does not match, the function sets `isPalindrome` to `false`. The function returns a tuple containing the result string and the `isPalindrome` boolean.