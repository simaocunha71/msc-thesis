    groups  := make([]string, 0)
    for i  := 0; i < ((len(s) + 2) / 3); i++  {
        groups  = append(groups, s[3*i:int(math.Min(float64(3*i+3), float64(len(s))))])
    }
    newGroups  := make([]string, 0)
    for _, group  := range groups  {
        runes  := []rune(group)
        if len(group) == 3  {
            newGroups  = append(newGroups, string(append([]rune{runes[2]}, runes[0:2]...)))
        } else  {
            newGroups  = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}




func main()  {
    testStr := "Hello, World!"

    fmt.Println("Original string: ", testStr)
    encodedStr := EncodeCyclic(testStr)
    fmt.Println("Encoded string: ", encodedStr)
    decodedStr := DecodeCyclic(encodedStr)
    fmt.Println("Decoded string: ", decodedStr)
}



A: You can use the following code to encode and decode your string:

```go
package main

import (
    "fmt"
    "strings"
)

func encode(s string) string {
    var encoded strings.Builder
    for i := 0; i < len(s); i += 3 {
        end := i + 3
        if end > len(s) {
            end = len(s)
        }
        group := s[i:end]
        encoded.WriteString(group[1:])
        encoded.WriteString(group[:1])
    }
    return encoded.String()
}

func decode(s string) string {
    var decoded strings.Builder
    for i := 0; i < len(s); i += 3 {
        end := i + 3
        if end > len(s