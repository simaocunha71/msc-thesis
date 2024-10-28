You can solve this problem by using a stack to keep track of the brackets. When you encounter an opening bracket, you push it onto the stack. When you encounter a closing bracket, you check if the stack is empty or if the top of the stack is not the corresponding opening bracket. If either of these conditions is true, then the brackets are not correctly balanced.

Here is the code:

```
func CorrectBracketing(brackets string) bool {
    stack := make([]rune, 0)
    for _, b := range brackets {
        if b == '(' || b == '[' || b == '{' {
            stack = append(stack, b)
        } else if b == ')' {
            if len(stack) == 0 || stack[len(stack)-1] != '(' {
                return false
            }
            stack = stack[:len(stack)-1]
        } else if b == ']' {
            if len(stack) == 0 || stack[len(stack)-1] != '[' {
                return false
            }
            stack = stack[:len(stack)-1]
        } else if b == '}' {
            if len(stack) == 0 || stack[len(stack)-1] != '{' {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```

This code should correctly determine if the brackets are balanced or not.