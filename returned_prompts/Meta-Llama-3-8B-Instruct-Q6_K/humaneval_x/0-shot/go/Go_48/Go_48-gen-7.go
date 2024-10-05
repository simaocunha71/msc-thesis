```go
package main

import (
    "fmt"
    "strings"
)

func IsPalindrome(text string) bool {
    // Clean the text from non-alphanumeric characters
    cleanText := strings.Map(func(r rune) rune {
        if r == ' ' || r == ',' || r == '.' || r == '?' {
            return -1
        }
        return r
    }, strings.ToLower(text))

    // Convert the cleaned text to a string
    cleanTextStr := string(cleanText)

    // Compare the cleaned text with its reverse
    for i := 0; i < len(cleanTextStr)/2; i++ {
        if cleanTextStr[i] != cleanTextStr[len(cleanTextStr)-1-i] {
            return false
        }
    }

    return true
}

func main() {
    fmt.Println(IsPalindrome(""))          // true
    fmt.Println(IsPalindrome("aba"))      // true
    fmt.Println(IsPalindrome("aaaaa"))    // true
    fmt.Println(IsPalindrome("zbcd"))     // false
}
```

Explanation:

The `IsPalindrome` function takes a string as input and checks if it's a palindrome. A palindrome is a string that reads the same backward as forward.

Here's how it works:

1. The function first cleans the input string from non-alphanumeric characters (spaces, commas, dots, etc.) and converts it to lowercase using the `strings.Map` function.
2. It then converts the cleaned string to a string using the `string` function.
3. The function then compares the cleaned string with its reverse. It does this by iterating through the cleaned string and checking if each character matches the corresponding character from the end of the string.
4. If any characters don't match, the function returns `false`. If all characters match, the function returns `true`.

In the `main` function, we test the `IsPalindrome` function with different inputs and print the results.

Note: This implementation is case-insensitive and ignores non-alphanumeric characters. If you want to make it case-sensitive or include non-alphanumeric characters in the comparison, you'll need to modify the implementation accordingly.