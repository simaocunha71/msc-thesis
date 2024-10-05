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

	if len(brackets) == 0 {
		return true
	}

	for i := 0; i < len(brackets); i++ {
		if brackets[i] == '(' {
			if i == len(brackets)-1 || brackets[i+1] != ')' {
				return false
			}
			i++
		}
	}

	return true
}



