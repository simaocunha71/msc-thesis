```go
package main

import (
    "strings"
)

func CountDistinctCharacters(str string) int {
    str = strings.ToLower(str)
    charSet := make(map[rune]bool)
    for _, char := range str {
        charSet[char] = true
    }
    return len(charSet)
}

func main() {
    println(CountDistinctCharacters("xyzXYZ")) // Output: 3
    println(CountDistinctCharacters("Jerry")) // Output: 4
}
```
In this code, we first convert the input string to lowercase using `strings.ToLower` to ignore the case of the characters. Then we create a map (`charSet`) to store the characters. We iterate over the characters in the string and add each character to the map. Since maps in Go do not allow duplicate keys, this effectively gives us a set of distinct characters. Finally, we return the size of the map, which is the number of distinct characters in the string.

In the `main` function, we call `CountDistinctCharacters` with two test strings and print the results. The output is `3` for `"xyzXYZ"` and `4` for `"Jerry"`, which are the correct counts of distinct characters.