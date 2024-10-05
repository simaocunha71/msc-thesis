Here is the solution using a stack data structure:
```go
import (
    "strings"
)

func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, bracket := range brackets {
        if bracket == '(' {
            stack = append(stack, '(')
        } else if bracket == ')' {
            if len(stack) == 0 || stack[len(stack)-1] != '(' {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```
Here's an explanation of the code:

* We create an empty stack `stack` to keep track of the opening brackets.
* We iterate through each character `bracket` in the input string `brackets`.
* If `bracket` is an opening bracket `(`, we push it onto the stack.
* If `bracket` is a closing bracket `)`, we check if the stack is empty or if the top of the stack is not an opening bracket. If either condition is true, we return `false` because there is no corresponding opening bracket. Otherwise, we pop the opening bracket from the stack.
* After iterating through all characters, we check if the stack is empty. If it is, it means every opening bracket had a corresponding closing bracket, so we return `true`. Otherwise, we return `false`.