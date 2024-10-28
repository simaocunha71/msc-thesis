Here is a Go solution that uses a stack to keep track of the parentheses:

```go
func SeparateParenGroups(paren_string string) []string {
    stack := []int{}
    groups := [][]int{}
    for i := range paren_string {
        if paren_string[i] == '(' {
            stack = append(stack, i)
        } else if paren_string[i] == ')' {
            if len(stack) == 0 {
                continue
            }
            start := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            groups = append(groups, []int{start, i})
        }
    }
    result := make([]string, len(groups))
    for i, group := range groups {
        result[i] = paren_string[group[0]:group[1]+1]
    }
    return result
}
```

This solution works by iterating over the input string and pushing the index of each opening parenthesis onto the stack. When it encounters a closing parenthesis, it pops the last index from the stack and adds the group of parentheses (from the popped index to the current index) to the list of groups.

After processing the entire string, it constructs the result by taking each group of parentheses and extracting the substring from the input string.

Here's an example of how to use this function:

```go
func main() {
    paren_string := "( ) (( )) (( )( ))"
    result := SeparateParenGroups(paren_string)
    fmt.Println(result) // Output: ["()", "(())", "(()())"]
}
```