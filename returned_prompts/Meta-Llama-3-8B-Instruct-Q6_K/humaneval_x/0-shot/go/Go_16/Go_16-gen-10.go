```go
package main

import (
    "strings"
    "fmt"
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
    fmt.Println(CountDistinctCharacters("xyzXYZ")) // 3
    fmt.Println(CountDistinctCharacters("Jerry")) // 4
}
```


Explanation:

*   We use the `strings.ToLower()` function to convert the input string to lowercase. This allows us to ignore the case of the characters when counting distinct characters.
*   We create a `map` called `charSet` to store the unique characters. The key is the character itself, and the value is `true` to indicate that the character has been seen.
*   We iterate over the characters in the input string using a `for` loop. For each character, we check if it's already present in the `charSet` using the `ok` variable. If it's not present, we add it to the `charSet`.
*   Finally, we return the length of the `charSet`, which represents the number of distinct characters in the input string.
*   In the `main` function, we test the `CountDistinctCharacters` function with the input strings "xyzXYZ" and "Jerry", and print the results to the console.