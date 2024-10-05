    groups := make([]string, 0)
    for i := 0; i < ((len(s) + 2) / 3); i++ {
        groups = append(groups, s[3*i:int(math.Min(float64(3*i+3), float64(len(s))))])
    }
    newGroups := make([]string, 0)
    for _, group := range groups {
        runes := []rune(group)
        if len(group) == 3 {
            newGroups = append(newGroups, string(append([]rune{runes[2]}, runes[0:2]...)))
        } else {
            newGroups = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}

func main() {
    s := "Hello, World!"
    encoded := EncodeCyclic(s)
    decoded := DecodeCyclic(encoded)
    fmt.Println("Original: ", s)
    fmt.Println("Encoded: ", encoded)
    fmt.Println("Decoded: ", decoded)
}

*/
package main

import (
	"fmt"
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