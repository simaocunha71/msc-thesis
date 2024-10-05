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
    println(CountDistinctCharacters("xyzXYZ")) // prints 3
    println(CountDistinctCharacters("Jerry")) // prints 4
}
```


In this solution, we first convert the string to lowercase using the `strings.ToLower` function. Then we create a map `charSet` to store the distinct characters. We iterate over the string, and for each character, we check if it's already present in the `charSet`. If it's not, we add it to the `charSet`. Finally, we return the length of the `charSet`, which represents the number of distinct characters in the string.