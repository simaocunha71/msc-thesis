```go
package main

import (
    "strings"
    "fmt"
)

// Given a string, find out how many distinct characters (regardless of case) does it consist of
func CountDistinctCharacters(str string) int {
    str = strings.ToLower(str)
    charSet := make(map[rune]bool)
    for _, char := range str {
        charSet[char] = true
    }
    return len(charSet)
}

func main() {
    fmt.Println(CountDistinctCharacters("xyzXYZ"))  // Output: 3
    fmt.Println(CountDistinctCharacters("Jerry"))  // Output: 4
}
```

Explanation:

1. We first convert the input string to lowercase using `strings.ToLower` to ensure the comparison is case-insensitive.
2. We create a `map[rune]bool` called `charSet` to store the distinct characters.
3. We iterate over each character in the input string using a range loop. For each character, we add it to the `charSet` map.
4. The `len` function returns the number of distinct characters in the `charSet` map, which is the desired output.

The `main` function demonstrates the usage of the `CountDistinctCharacters` function with two examples. The output for each example is printed to the console.