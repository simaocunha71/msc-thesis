You can use a stack to solve this problem. Here's how you can do it:

```go
func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, b := range brackets {
        if b == '(' {
            stack = append(stack, b)
        } else if len(stack) == 0 || stack[len(stack)-1] != '(' {
            return false
        } else {
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```

Explanation:
- We iterate over the string `brackets` character by character.
- If we encounter an opening bracket `'('`, we push it onto the stack.
- If we encounter a closing bracket `')'`, we check if the stack is empty or the top element of the stack is not an opening bracket `'('`. If either of these conditions is true, we return `false` because it means that there is no corresponding opening bracket for this closing bracket.
- If we encounter an opening bracket `'('` or a closing bracket `')'` that has a corresponding opening bracket on top of the stack, we pop the top element from the stack.
- After we have processed all characters in `brackets`, we check if the stack is empty. If it is, it means that all opening brackets have corresponding closing brackets, so we return `true`. Otherwise, we return `false` because there are some opening brackets without corresponding closing brackets.