    groups := make([]string, 0)
    for i:=0; i<((len(s)+2)/3); i++ {
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

// takes as input two strings, returns true if they are equal after encoding and decoding.
func IsEqual(s1 string, s2 string) bool {
    return DecodeCyclic(EncodeCyclic(s1)) == DecodeCyclic(EncodeCyclic(s2))
}

// takes as input two strings, returns true if they are equal after encoding and decoding.
// does not use DecodeCyclic function.
func IsEqualWithoutDecode(s1 string, s2 string) bool {
    encoded1 := EncodeCyclic(s1)
    encoded2 := EncodeCyclic(s2)
    return encoded1 == encoded2
}

I have a test:
package main

import (
    "fmt"
    "time"
)

func main() {
    s := "some long string to test the function"
    encoded := EncodeCyclic(s)
    decoded := DecodeCyclic(encoded)
    fmt.Println(s)
    fmt.Println(encoded)
    fmt.Println(decoded)
    fmt.Println(IsEqual(s, decoded))
    fmt.Println(IsEqualWithoutDecode(s, decoded))
}

The result is:
some long string to test the function
o