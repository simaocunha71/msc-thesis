```go
package main

import (
    "strings"
)

func CountDistinctCharacters(str string) int {
    str = strings.ToLower(str)
    charSet := make(map[rune]bool)
    for _, char := range str {
        if _, ok := charSet[char]; !ok {
            charSet[char] = true
        }
    }
    return len(charSet)
}

func main() {
    println(CountDistinctCharacters("xyzXYZ")) // Output: 3
    println(CountDistinctCharacters("Jerry")) // Output: 4
}
```
Explanation:
1. We first convert the input string to lowercase using `strings.ToLower` function to ensure case-insensitivity.
2. We create an empty map `charSet` of type `map[rune]bool` to store unique characters.
3. We iterate through each character in the string using a range loop.
4. For each character, we check if it already exists in the `charSet` using the comma, ok idiom. If the character is not present in the map, we add it to the map.
5. Finally, we return the length of the `charSet`, which represents the number of distinct characters in the input string.

In the example code, we define a function `CountDistinctCharacters` that takes a string as input and returns the number of distinct characters. We then call this function with two test strings and print the results. The output should be `3` for the string "xyzXYZ" and `4` for the string "Jerry".