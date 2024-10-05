Here is the solution:
```
func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, r := range brackets {
        if r == '(' {
            stack = append(stack, r)
        } else if r == ')' {
            if len(stack) == 0 || stack[len(stack)-1] != '(' {
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
* We iterate through the input string, character by character.
* When we encounter an opening bracket `(`, we push it onto the stack.
* When we encounter a closing bracket `)`, we check if the stack is empty or if the top element of the stack is not an opening bracket. If either condition is true, we return `false`.
* If the stack is not empty and the top element is an opening bracket, we pop it from the stack.
* Finally, we check if the stack is empty. If it is, it means all opening brackets have corresponding closing brackets, so we return `true`. Otherwise, we return `false`.