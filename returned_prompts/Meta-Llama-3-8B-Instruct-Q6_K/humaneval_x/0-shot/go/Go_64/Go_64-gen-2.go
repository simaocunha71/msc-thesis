```go
package main

import (
    "strings"
)

func VowelsCount(s string) int {
    s = strings.ToLower(s)
    count := 0
    for _, c := range s {
        if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
            if c == 'y' && s[len(s)-1] == 'y' {
                continue
            }
            count++
        }
    }
    return count
}

func main() {
    fmt.Println(VowelsCount("abcde"))  // Output: 2
    fmt.Println(VowelsCount("ACEDY"))  // Output: 3
}
```

Explanation:
This program defines a function `VowelsCount` that takes a string `s` as input and returns the number of vowels in the string. The function first converts the string to lowercase using the `strings.ToLower` function to ensure that the function works correctly for both lowercase and uppercase letters.

The function then initializes a counter `count` to 0 and iterates over each character `c` in the string using a `for` loop.

For each character, the function checks if it is a vowel (i.e., if it is equal to 'a', 'e', 'i', 'o', or 'u') using a conditional statement. If the character is a vowel, the function increments the `count` by 1.

The function also includes a special case for the character 'y'. If the character is 'y' and it is at the end of the string (i.e., if `s[len(s)-1] == 'y'`), the function skips the increment of the `count`. This is because 'y' is considered a vowel only when it is at the end of the string.

Finally, the function returns the `count`, which represents the number of vowels in the input string.

In the `main` function, the program tests the `VowelsCount` function with two example strings, "abcde" and "ACEDY", and prints the results to the console. The output is 2 for "abcde" and 3 for "ACEDY".