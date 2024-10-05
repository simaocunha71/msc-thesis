```go
package main

import "fmt"

func IsPalindrome(text string) bool {
    // Convert the string to lower case
    text = strings.ToLower(text)
    // Remove spaces and punctuation
    text = strings.Map(func(r rune) rune {
        if r == ' ' || r == '.' || r == ',' || r == '?' || r == '!' {
            return -1
        }
        return r
    }, text)
    // Remove non-alphanumeric characters
    text = strings.Map(func(r rune) rune {
        if r >= 'a' && r <= 'z' || r >= '0' && r <= '9' {
            return r
        }
        return -1
    }, text)
    // Check if the string is equal to its reverse
    return text == reverse(text)
}

func reverse(text string) string {
    runes := []rune(text)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func main() {
    fmt.Println(IsPalindrome(""))          // true
    fmt.Println(IsPalindrome("aba"))      // true
    fmt.Println(IsPalindrome("aaaaa"))    // true
    fmt.Println(IsPalindrome("zbcd"))     // false
}
```

Explanation:

1.  We first convert the input string to lowercase using `strings.ToLower`.
2.  Then, we remove spaces and punctuation using `strings.Map`. We replace these characters with an empty string (`""`).
3.  Next, we remove non-alphanumeric characters using `strings.Map`. We replace these characters with an empty string (`""`).
4.  After that, we check if the resulting string is equal to its reverse using the `reverse` function.
5.  The `reverse` function simply reverses the input string by swapping its characters.
6.  Finally, we print the results for the given test cases. The `main` function calls `IsPalindrome` with different input strings and prints the results using `fmt.Println`.