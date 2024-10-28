To encode the string you're cycling groups of three characters, and to decode you need to reverse the process.

For example, given the string "abcde" the encoding would be "cdeaba".

To reverse the process, you can follow these steps:

- Get all the three-character groups from the string. For example, from the string "cdeaba" you would get "cde", "aba".
- If the group is a single character, then move the character to the front of the group. For example, "cde" becomes "ecd".
- Join the resulting groups to obtain the original string.

Here is a possible implementation of the above steps in Go:

```go
package main

import (
    "fmt"
    "strings"
)

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

func DecodeCyclic(s string) string {
    groups := make([]string, 0)
    for i := 0; i < len(s); i += 3 {
        groups = append(groups, s[i:i+3])
    }
    newGroups := make([]string, 0)
    for _, group := range groups {
        runes := []rune(group)
        if len(group) == 1 {
            newGroups = append(newGroups, string(append(runes[0:], runes[len(group)-1])))
       