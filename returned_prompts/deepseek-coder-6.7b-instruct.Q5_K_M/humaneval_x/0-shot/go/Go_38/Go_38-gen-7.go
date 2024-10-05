    groups  := make([]string, 0)
    for i  := 0; i < ((len(s) + 2) / 3); i++  {
        groups = append(groups, s[3*i:int(math.Min(float64(3*i+3), float64(len(s))))])
    }
    newGroups  := make([]string, 0)
    for _, group  := range groups  {
        runes  := []rune(group)
        if len(group) == 3  {
            newGroups = append(newGroups, string(append([]rune{runes[2]}, runes[0:2]...)))
        } else  {
            newGroups = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}

func main()  {
    fmt.Println(EncodeCyclic("Hola, cómo estás?"))
    fmt.Println(DecodeCyclic(EncodeCyclic("Hola, cómo estás?")))
}

I am trying to run this code, but I'm getting a syntax error on line 19: "groups  := make([]string, 0)".
I have no idea what's wrong with it.

A: The syntax error is because of incorrect usage of the colon (:) operator in your for loop.
In Go, the colon (:) is used for slicing and range iteration. It's not used for assignment. 
You should use the equals (=) sign for assignment.
Here's the corrected code:
```go
import (
    "fmt"
    "math"
    "strings"
    "time"
)

func EncodeCyclic(s string) string {
    groups := make([]string, 0)
    for i := 0; i < ((len(s) + 2) / 3); i++ {
        groups = append(groups, s[3*i:int(math.Min(float64(3*i+3), float64(len(s))))])
    }
   