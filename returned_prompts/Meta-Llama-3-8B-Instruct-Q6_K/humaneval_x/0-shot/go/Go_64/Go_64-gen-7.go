```go
package main

import (
    "strings"
)

func VowelsCount(s string) int {
    s = strings.ToLower(s)
    count := 0
    for _, char := range s {
        if char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u' {
            count++
        }
    }
    // check if 'y' is at the end of the string
    if len(s) > 0 && (s[len(s)-1] == 'y') {
        count++
    }
    return count
}

func main() {
    println(VowelsCount("abcde"))  // Output: 2
    println(VowelsCount("ACEDY"))  // Output: 3
}
```

Explanation:
We use the `strings.ToLower` function to convert the input string to lowercase. This is to ensure that we treat 'A' and 'a' as the same vowel.

We then use a for loop to iterate over each character in the string. We check if the character is one of the vowels ('a', 'e', 'i', 'o', 'u') and if so, increment the count.

Finally, we check if the last character of the string is 'y'. If it is, we increment the count again. This is because 'y' is considered a vowel when it is at the end of the string.

The function returns the total count of vowels in the string. In the main function, we test the function with the examples provided.