Here is the solution in Go:

```go
package main

import (
    "math"
    "strings"
    "time"
)

// returns encoded string by cycling groups of three characters.
func EncodeCyclic(s string) string {
    groups := make([]string, 0)
    for i := 0; i < ((len(s) + 2) / 3); i++ {
        groups = append(groups, s[3*i:int(math.Min(float64(3*i+3), float64(len(s))))])
    }
    newGroups := make([]string, 0)
    for _, group := range groups {
        runes := []rune(group)
        if len(group) == 3 {
            newGroups = append(newGroups, string(append(runes[1:], runes[0])))
        } else {
            newGroups = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}

// takes as input string encoded with EncodeCyclic function. Returns decoded string.
func DecodeCyclic(s string) string {
    groups := make([]string, 0)
    for i := 0; i < ((len(s) + 2) / 3); i++ {
        groups = append(groups, s[i*3:(i+1)*3])
    }
    newGroups := make([]string, 0)
    for _, group := range groups {
        runes := []rune(group)
        if len(group) == 3 {
            newGroups = append(newGroups, string(append([]rune{runes[0]}, runes[1:]...)))
        } else {
            newGroups = append(newGroups, group)
        }
    }
    result := ""
    for _, group := range newGroups {
        result += group
    }
    return result
}

func main() {
    s := "Hello, World!"
    encoded := EncodeCyclic(s)
    decoded := DecodeCyclic(encoded)
    if decoded == s {
        println("Encoded and decoded strings are equal.")
    } else {
        println("Encoded and decoded strings are not equal.")
    }
}
```

This program defines two functions, EncodeCyclic and DecodeCyclic. The EncodeCyclic function takes a string as input, breaks it into groups of three characters, and then shifts each group one character to the right. The DecodeCyclic function reverses this process, shifting each group one character to the left. In the main function, a test string