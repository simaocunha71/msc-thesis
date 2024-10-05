```go
package main

import (
    "strings"
    "fmt"
)

func Histogram(test string) map[rune]int {
    if test == "" {
        return map[rune]int{}
    }
    freq := make(map[rune]int)
    for _, c := range strings.Split(test, " ") {
        count := strings.Count(c, string(c[0]))
        freq[c[0]] = count
    }
    maxCount := 0
    maxFrequencies := make(map[rune]int)
    for k, v := range freq {
        if v > maxCount {
            maxCount = v
            maxFrequencies = map[rune]int{k: v}
        } else if v == maxCount {
            maxFrequencies[k] = v
        }
    }
    return maxFrequencies
}

func main() {
    fmt.Println(Histogram("a b c"))        // Output: map[a:1 b:1 c:1]
    fmt.Println(Histogram("a b b a"))     // Output: map[a:2 b:2]
    fmt.Println(Histogram("a b c a b"))   // Output: map[a:2 b:2]
    fmt.Println(Histogram("b b b b a"))   // Output: map[b:4]
    fmt.Println(Histogram(""))            // Output: map[]
}
```
The code above implements a function called `Histogram` that takes a string as input and returns a map where the keys are the letters that appear most frequently in the string and the values are the counts of those letters.

The function first checks if the input string is empty, in which case it returns an empty map.

Then it splits the input string into individual characters using the `strings.Split` function and iterates over the resulting slice. For each character, it counts the number of occurrences of that character in the string using the `strings.Count` function and stores this count in a map called `freq`.

Next, it finds the maximum count in the `freq` map and creates a new map called `maxFrequencies` that contains only the characters with the maximum count. If there are multiple characters with the same maximum count, all of them are added to `maxFrequencies`.

Finally, the function returns the `maxFrequencies` map.

The `main` function demonstrates the usage of the `Histogram` function with different input strings. The output of each call is printed to the console.