Here is the solution using a stack:
```go
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
    stack := []rune{}
    for _, rune := range brackets {
        if rune == '(' {
            stack = append(stack, rune)
        } else if rune == ')' {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```
Explanation:

We use a stack to keep track of the opening brackets. We iterate through the string, and for each character:

* If it's an opening bracket `(`, we push it onto the stack.
* If it's a closing bracket `)`, we check if the stack is empty. If it is, it means there's no corresponding opening bracket, so we return `false`. Otherwise, we pop the opening bracket from the stack.
* After iterating through the entire string, we check if the stack is empty. If it is, it means every opening bracket had a corresponding closing bracket, so we return `true`. Otherwise, we return `false`.