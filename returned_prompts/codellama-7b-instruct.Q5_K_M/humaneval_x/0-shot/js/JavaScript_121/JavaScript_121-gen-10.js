import (
    "fmt"
    "strings"
)

// brackets is a string of "(" and ")".
// return true if every opening bracket has a corresponding closing bracket.
// 
// >>> CorrectBracketing("(")
// false
// >>> CorrectBracketing("()")
// true
// >>> CorrectBracketing("(()())")
// true
// >>> CorrectBracketing(")(()")
// false
func CorrectBracketing(brackets string) bool {
    var stack []string
    for _, bracket := range brackets {
        if bracket == "(" {
            stack = append(stack, "(")
        } else if bracket == ")" {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}

func main() {
    fmt.Println(CorrectBracketing("("))
    fmt.