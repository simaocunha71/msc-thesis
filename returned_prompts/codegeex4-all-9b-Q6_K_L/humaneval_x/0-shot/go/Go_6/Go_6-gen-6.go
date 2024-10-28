Here's the solution that solves the problem:

```go
func ParseNestedParens(paren_string string) []int {
    var groups []string = strings.Split(paren_string, " ")
    var max_levels []int = make([]int, len(groups))
    
    for i, group := range groups {
        max_level := 0
        current_level := 0
        for _, c := range group {
            if c == '(' {
                current_level++
                if current_level > max_level {
                    max_level = current_level
                }
            } else if c == ')' {
                current_level--
            }
        }
        max_levels[i] = max_level
    }
    return max_levels
}
```

This function first splits the input string into groups using the space character as a delimiter. For each group, it traverses each character and if it encounters an opening parenthesis `(`, it increases the current level. If it encounters a closing parenthesis `)`, it decreases the current level. It keeps track of the maximum level encountered and returns it as the deepest level of nesting for that group.