Here is a possible solution using a stack to keep track of the parentheses and their nesting level:

```go
func SeparateParenGroups(paren_string string) []string {
    stack := make([]struct {
        level int
        start int
    }, 0)
    groups := make([]string, 0)
    for i, c := range paren_string {
        if c == '(' {
            stack = append(stack, struct {
                level int
                start int
            }{len(stack), i})
        } else if c == ')' {
            if len(stack) == 0 {
                panic("Mismatched parentheses")
            }
            top := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            if len(stack) == 0 || stack[len(stack)-1].level < top.level {
                groups = append(groups, paren_string[top.start:i+1])
            }
        }
    }
    if len(stack) > 0 {
        panic("Mismatched parentheses")
    }
    return groups
}
```

This function uses a stack to keep track of the parentheses and their nesting level. It iterates through the input string and whenever it encounters an open parenthesis, it pushes a new element onto the stack with the current nesting level and the index of the open parenthesis. When it encounters a close parenthesis, it checks if there is a matching open parenthesis on the stack. If there is, it pops the top element from the stack and if it is the outermost group (i.e., its nesting level is equal to the length of the stack minus one), it adds the substring of the input string from the start index of the group to the current index (inclusive) to the list of groups. If there is no matching open parenthesis, it panics.

After iterating through the entire input string, the function checks if there are any unmatched open parentheses left on the stack. If there are, it panics. Finally, it returns the list of groups.

This solution has a time complexity of O(n), where n is the length of the input string, because it iterates through the input string once. It has a space complexity of O(n), because it uses a stack to keep track of the parentheses and their nesting level, and a list to store the groups.