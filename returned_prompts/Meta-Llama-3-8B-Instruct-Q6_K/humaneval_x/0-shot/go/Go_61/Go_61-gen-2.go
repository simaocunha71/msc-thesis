Here is a simple and efficient solution using a stack data structure:
```go
func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, bracket := range brackets {
        if bracket == '(' {
            stack = append(stack, bracket)
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

1. We create an empty stack `[]rune{}` to keep track of the opening brackets.
2. We iterate through each character in the input string `brackets`.
3. If we encounter an opening bracket `(`, we push it onto the stack.
4. If we encounter a closing bracket `)`, we check if the stack is empty or if the top element of the stack is not an opening bracket. If either of these conditions is true, we return `false`.
5. If the stack is not empty and the top element is an opening bracket, we pop it from the stack.
6. Finally, we return `true` if the stack is empty (i.e., all opening brackets have been matched with closing brackets) and `false` otherwise.

This solution has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(n) due to the stack.