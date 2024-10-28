func CorrectBracketing(brackets string) bool {
    count := 0
    for _, c := range brackets {
        if c == '(' {
            count++
        } else if c == ')' {
            count--
        }
        if count < 0 {
            return false
        }
    }
    return count == 0
}

B:
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
    count := 0
    for _, c := range brackets {
        if c == '(' {
            count++
        } else if c == ')' {
            count--
        }
        if count < 0 {
            return false
        }
    }
    return count == 0
}

C:
func CorrectBracketing(brackets string) bool {
    count := 0
    for _, c := range brackets {
        if c == '(' {
            count++
        } else if c == ')' {
            count--
        }
        if count < 0 {
            return false
        }
    }
    return count == 0
}

D:
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
    count := 0
    for _, c := range brackets {
        if c == '(' {
            count++
        } else if c == ')' {
            count--
        }
        if count < 0 {
            return false
        }
    }
    return count == 0
}

E:
func CorrectBracketing(brackets string) bool {
    count := 0
    for _, c := range brackets {
        if c == '(' {
            count++
        } else if c == ')' {
            count--
        }
        if count < 0 {
            return false
        }
    }
    return count == 0
}

F:
import (
    "strings"
)

