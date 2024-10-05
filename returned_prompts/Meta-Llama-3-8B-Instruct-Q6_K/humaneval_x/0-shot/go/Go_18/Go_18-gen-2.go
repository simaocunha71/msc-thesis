```go
package main

import (
    "fmt"
    "strings"
)

func HowManyTimes(str string, substring string) int {
    count := 0
    for i := 0; i <= len(str)-len(substring); i++ {
        if strings.Compare(str[i:i+len(substring)], substring) == 0 {
            count++
        }
    }
    return count
}

func main() {
    fmt.Println(HowManyTimes("", "a"))  // 0
    fmt.Println(HowManyTimes("aaa", "a"))  // 3
    fmt.Println(HowManyTimes("aaaa", "aa"))  // 3
}
```

The function HowManyTimes takes two parameters: a string and a substring. It counts the number of times the substring appears in the string. If the substring does not appear in the string, the function returns 0.

The function works by iterating over the string, checking each substring of the same length as the given substring to see if it matches. It uses the strings.Compare function to compare the current substring with the given substring, and if they match, increments the count. If the current substring is longer than the given substring, it breaks out of the loop and returns the count.

In the main function, the function HowManyTimes is called with different input parameters and the results are printed to the console. The function correctly returns 0 for the empty string, 3 for the string "aaa" and the substring "a", and 3 for the string "aaaa" and the substring "aa".