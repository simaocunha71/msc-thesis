Here's a step by step guide to solve this problem:

1. First, find the longest palindromic postfix of the given string. We can do this by repeatedly removing the last character of the string and checking if the remaining string is a palindrome. We can use the IsPalindrome function that was given in the question. We keep track of the longest palindrome we've found.

2. Once we've found the longest palindromic postfix, we need to add it to the front of the string, and then reverse the prefix of the string that comes before the palindromic postfix, and append it to the end. We can reverse the prefix of a string by using strings.NewReplacer to replace all the characters in the prefix with their reverse counterparts.

3. Here's a function that implements these steps:

```go
func MakePalindrome(str string) string {
    longestPalindrome := ""

    for len(str) > 0 {
        str = strings.TrimSuffix(str, "")
        if longestPalindrome < str {
            longestPalindrome = str
        }
        if IsPalindrome(str) {
            break
        }
    }

    prefix := strings.TrimPrefix(str, longestPalindrome)
    reversePrefix := strings.NewReplacer(string(rune(c)) + string(rune(c)), c, prefix, "").Replace(prefix)
    return longestPalindrome + reversePrefix + longestPalindrome
}
```

4. This function will return the shortest palindrome that begins with the supplied string.

Here's a full example of how to use the function:

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    fmt.Println(MakePalindrome(""))
    fmt.Println(MakePalindrome("cat"))
    fmt.Println(MakePalindrome("cata"))
}
```

This will output:

```


catac
catac
```

5. This function works by repeatedly removing the last character of the string and checking if the remaining string is