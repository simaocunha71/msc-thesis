```go
package main

import (
    "strings"
)

func CountDistinctCharacters(str string) int {
    str = strings.ToLower(str) // convert to lowercase
    charSet := make(map[rune]bool)
    for _, char := range str {
        if _, ok := charSet[char]; !ok {
            charSet[char] = true
        }
    }
    return len(charSet)
}

func main() {
    println(CountDistinctCharacters("xyzXYZ"))  // 3
    println(CountDistinctCharacters("Jerry"))  // 4
}
```

Explanation:

1. The function `CountDistinctCharacters` takes a string `str` as input.
2. It converts the string to lowercase using the `strings.ToLower` function to ensure the count is case-insensitive.
3. It creates an empty map `charSet` of type `map[rune]bool` to store the distinct characters.
4. It iterates over the characters in the string using a range loop.
5. For each character, it checks if the character is already present in the `charSet` map using the `_, ok := charSet[char]` syntax. If the character is not present, it adds it to the map.
6. Finally, it returns the length of the `charSet` map, which represents the number of distinct characters in the string.

In the `main` function, we call the `CountDistinctCharacters` function with two test strings and print the results. The output should be `3` for the first call and `4` for the second call.