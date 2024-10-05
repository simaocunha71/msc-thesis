```
package main
import "fmt"

func CycpatternCheck(a, b string) bool {
    for i := 0; i < len(b); i++ {
        b1 := b[i:]
        if len(b1) > len(a) {
            return false
        }
        if contains(a, b1) {
            return true
        }
    }
    return false
}

func contains(a, b string) bool {
    for i := 0; i < len(a); i++ {
        if a[i:i+len(b)] == b {
            return true
        }
    }
    return false
}

func main() {
    fmt.Println(CycpatternCheck("abcd", "abd")) // => false
    fmt.Println(CycpatternCheck("hello", "ell")) // => true
    fmt.Println(CycpatternCheck("whassup", "psus")) // => false
    fmt.Println(CycpatternCheck("abab", "baa")) // => true
    fmt.Println(CycpatternCheck("efef", "eeff")) // => false
    fmt.Println(CycpatternCheck("himenss", "simen")) // => true
}
```


This program checks if the second word or any of its rotations is a substring in the first word. It uses two helper functions: `CycpatternCheck` and `contains`. `CycpatternCheck` iterates over the characters in the second word, and for each character, it creates a new string that is a rotation of the second word. It then checks if this rotation is a substring of the first word using the `contains` function. If it is, it returns `true`. If it doesn't find a match after checking all rotations, it returns `false`. The `contains` function simply checks if the second word is a substring of the first word. It does this by iterating over the characters in the first word and checking if the substring of the second word matches the current substring of the first word. If it does, it returns `true`. If it doesn't find a match after checking all substrings, it returns `false`. The program then tests these functions with the given test cases.