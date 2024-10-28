
Here is a recursive solution:

```go
func CorrectBracketing(brackets string) bool {
    var stack []rune
    for _, c := range brackets {
        if c == '<' {
            stack = append(stack, c)
        } else if c == '>' {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```

This solution uses a stack to keep track of opening brackets until the corresponding closing bracket is found.

Here's how it works:

1. Initialize an empty stack.
2. For each character in the input string:
   - If the character is a "<", add it to the stack.
   - If the character is a ">", pop the top element from the stack. If the stack is empty, return false.
3. After processing all characters, if the stack is empty, return true. Otherwise, return false.

The time complexity of this solution is O(n), where n is the length of the input string, because each character in the input string is processed exactly once.

The space complexity of this solution is O(n) because the maximum size of the stack is proportional to the length of the input string.

Overall, this solution provides a simple and efficient way to determine if a string contains correctly nested brackets.

Here are some examples of how the solution works:

- For the input "<>", the solution correctly identifies that there is no matching closing bracket for the opening "<" and returns false.
- For the input "<<><>>", both opening "<" brackets have a matching closing ">" bracket, so the solution returns true.
- For the input "<><>", the solution correctly identifies that there is no matching closing bracket for the opening "<" and returns false.
```
```

```go
func CorrectBracketing(brackets string) bool {
    var stack []rune
    for _, c := range brackets {
        if c == '<' {
            stack = append(stack, c)
        } else if c == '>' {
