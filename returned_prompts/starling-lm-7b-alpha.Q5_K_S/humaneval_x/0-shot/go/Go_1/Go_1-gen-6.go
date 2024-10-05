To solve this problem we'll use a stack to keep track of the current group of parentheses. We'll also
keep track of the current level of the stack (number of open parentheses we have seen). When we see a
closed parenthesis, we'll check if it can match with the latest open parenthesis on the stack. If it does
match, we'll pop the open parenthesis off the stack. If it doesn't match, it means we've encountered a
nested group of parentheses, so we'll add the current string to the result list, then reset the stack and
start a new group.

Here's a step-by-step breakdown of the solution:

1. Initialize an empty stack and an empty result list.
2. Iterate over the input string, treating it as an array of characters. For each character, check if it's an
   open parenthesis '(':
   - If it is, push it onto the stack and increment the current level of the stack by 1.
3. If the character is a closed parenthesis ')':
   - Pop the latest open parenthesis from the stack. If the stack is empty at this point, it means there
     is no matching open parenthesis and we've found a nested group of parentheses. In this case, add the
     current string to the result list and reset the stack.
4. If the current level of the stack is 0, this means we've reached the end of a balanced group of
   parentheses. Add the current string to the result list and reset the stack.
5. Repeat steps 2-4 until all characters in the input string have been processed.
6. Return the result list containing all the balanced groups of parentheses.

Here's the implementation of the SeparateParenGroups function in Go:

```go
func SeparateParenGroups(paren_string string) []string {
    stack := make([]rune, 0)
    current_str := make([]rune, 0)
    current_level := 0

    for _, c := range paren_string {
        if c == '(' {
            stack = append(stack, c)
            current_level++
        } else if c == ')' {