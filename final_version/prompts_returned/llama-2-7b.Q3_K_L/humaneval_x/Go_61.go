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
    if brackets == "" {
        return true
    }
    
    leftBraceChar, rightBraceChar := "(", ")"
    for _, c := range []rune(leftBraceChar) {
        if !strings.ContainsRune(brackets, c) {
            return false
        }
    }
    for _, c := range []rune(rightBraceChar) {
        if !strings.ContainsRune(brackets, c) {
            return false
        }
    }
    
    return true
}