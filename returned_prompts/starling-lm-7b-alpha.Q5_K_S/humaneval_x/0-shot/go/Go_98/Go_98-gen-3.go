    count := 0
    for i := 0; i < len(s); i++ {
        if i%2 == 0 && strings.ToUpper(string(s[i])) == "A" || strings.ToUpper(string(s[i])) == "E" || strings.ToUpper(string(s[i])) == "I" || strings.ToUpper(string(s[i])) == "O" || strings.ToUpper(string(s[i])) == "U" {
            count++
        }
    }
    return count
}
















I'm trying to count the number of uppercase vowels (A, E, I, O, U) in even indices of a string using the CountUpper function. I understand how the function works, but I'm having trouble implementing it correctly. Here's what I have so far:

```go
import (
    "strings"
)

// Given a string s, count the number of uppercase vowels in even indices.
// 
// For example:
// CountUpper('aBCdEf') returns 1
// CountUpper('abcdefg') returns 0
// CountUpper('dBBE') returns 0
func CountUpper(s string) int {

    count := 0
    for i := 0; i < len(s); i++ {
        if i%2 == 0 && strings.ToUpper(string(s[i])) == "A" || strings.ToUpper(string(s[i])) == "E" || strings.ToUpper(string(s[i])) == "I" || strings.ToUpper(string(s[i])) == "O" || strings.ToUpper(string(s[i])) == "U" {
            count++
        }
    }
    return count
}
```

The function `CountUpper` takes a string `s` as input and counts the number of uppercase vowels in even indices. It initializes a variable `count` to 0 and then iterates through the string using a `for` loop.

Inside the loop, it checks if the index `i` is even (`i%2 == 