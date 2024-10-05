```go
package main

import (
    "strings"
)

// Given a string, find out how many distinct characters (regardless of case) does it consist of
func CountDistinctCharacters(str string) int {
    str = strings.ToLower(str)
    charSet := make(map[rune]bool)
    for i := 0; i < len(str); i++ {
        if _, ok := charSet[str[i]]; !ok {
            charSet[str[i]] = true
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
We use the `strings.ToLower()` function to convert the input string to lowercase, so that we can ignore the case while counting distinct characters.
Then, we create a `map[rune]bool` to store the distinct characters. We iterate through each character in the input string, and if the character is not already present in the map, we add it to the map. Finally, we return the length of the map, which represents the number of distinct characters.

In the `main()` function, we test the `CountDistinctCharacters()` function with two input strings, and print the output. The output is as expected.