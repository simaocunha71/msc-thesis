```
package main

import (
    "strings"
    "fmt"
)

func VowelsCount(s string) int {
    s = strings.ToLower(s)
    count := 0
    for _, char := range s {
        if char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u' {
            count++
        }
    }
    if s[len(s)-1] == 'y' {
        count++
    }
    return count
}

func main() {
    fmt.Println(VowelsCount("abcde")) // 2
    fmt.Println(VowelsCount("ACEDY")) // 3
}
```

The function VowelsCount first converts the input string to lowercase using the strings.ToLower function. Then, it iterates over each character in the string using a range-based for loop. If the character is a vowel (a, e, i, o, u), it increments a count variable. After iterating over all characters, it checks if the last character of the string is 'y'. If it is, it increments the count one more time. Finally, it returns the count.

In the main function, we test the VowelsCount function with the examples provided. The output is 2 for "abcde" and 3 for "ACEDY", as expected.