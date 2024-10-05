You can use a stack to keep track of the opening brackets. Iterate over the string, and for each character:

- If it's an opening bracket, push it onto the stack.
- If it's a closing bracket, check if the stack is empty. If it is, return false (because there's no corresponding opening bracket). If it's not empty, pop the opening bracket from the stack.

After iterating over the entire string, if the stack is empty, return true. If it's not, return false (because there are unmatched opening brackets).

Here's the implementation in Go:

```go
func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, bracket := range brackets {
        if bracket == '(' {
            stack = append(stack, bracket)
        } else if bracket == ')' {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```

This function uses a slice of runes (the type of which is `[]rune`) to simulate a stack. The `range` keyword is used to iterate over the characters in the input string. The `append` function is used to add an element to the stack, and the `[:len(stack)-1]` expression is used to remove the top element from the stack. The `len(stack) == 0` check is used to determine whether the stack is empty. If the stack is empty at the end of the function, it means that every opening bracket had a corresponding closing bracket, so the function returns `true`. If the stack is not empty, it means that there were unmatched opening brackets, so the function returns `false`. 