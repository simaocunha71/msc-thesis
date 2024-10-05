Here is a solution in Go that implements the MakePalindrome function:

```go
package main

import (
    "fmt"
    "strings"
    "unicode"
)

// Test if given string is a palindrome.
func IsPalindrome(str string) bool {
    runes := []rune(str)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        if runes[i] != runes[j] {
            return false
        }
    }
    return true
}

// Find the shortest palindrome that begins with a supplied string.
func MakePalindrome(str string) string {
    // Find the longest suffix of str that is a palindrome.
    for i := 0; i < len(str); i++ {
        suffix := str[i:]
        if IsPalindrome(suffix) {
            return str + reverse(str[:i])
        }
    }
    return str
}

// Reverse a string.
func reverse(str string) string {
    runes := []rune(str)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func main() {
    fmt.Println(MakePalindrome(""))  // Output: ""
    fmt.Println(MakePalindrome("cat"))  // Output: "catac"
    fmt.Println(MakePalindrome("cata"))  // Output: "catac"
}
```

The MakePalindrome function finds the longest suffix of the input string that is a palindrome, and then appends the reverse of the string prefix that comes before the palindromic suffix to the end of the string. The IsPalindrome function checks if a given string is a palindrome. The reverse function reverses a string. The main function demonstrates the usage of the MakePalindrome function. The output of the program will be as follows:

```
''
catac
catac
```

This solution works by iterating over the input string and checking each suffix to see if it is a palindrome. When a palindromic suffix is found, the function returns the original string plus the reverse of the prefix that comes before the palindromic suffix. This ensures that the resulting string is the shortest palindrome that begins with the original string. The IsPalindrome function is used to check if a given string is a palindrome, and the reverse function is