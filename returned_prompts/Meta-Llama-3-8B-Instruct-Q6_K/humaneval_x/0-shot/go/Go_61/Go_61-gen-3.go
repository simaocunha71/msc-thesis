Here is the solution:
```go
func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, r := range brackets {
        if r == '(' {
            stack = append(stack, r)
        } else if r == ')' {
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

* We use a stack to keep track of the opening brackets.
* We iterate over the string of brackets. For each character:
	+ If it's an opening bracket `(`, we push it onto the stack.
	+ If it's a closing bracket `)`, we check if the stack is empty. If it is, it means there's no corresponding opening bracket, so we return `false`. Otherwise, we pop the opening bracket from the stack.
* After iterating over the entire string, we check if the stack is empty. If it is, it means every opening bracket had a corresponding closing bracket, so we return `true`. If the stack is not empty, it means there were some opening brackets without corresponding closing brackets, so we return `false`.