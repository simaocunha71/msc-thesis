import (
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
    // split the brackets into two arrays: openings and closures.
    l := strings.Split(brackets, ")")

    // for each opening...
    for i, opn := range l {
        if !strings.Contains(opn, "(") {
            return false
        } else {
            i += 1
        }
    }
    cls := strings.Repeat(")", len(l))
    for i, close := range cls {
        if i+1 >= len(brackets) || !strings.Contains(close, "(") {
            return false
        } else {
            i += 1
        }
    }
    // if all is well, the arrays contain matching brackets:
    return true
}