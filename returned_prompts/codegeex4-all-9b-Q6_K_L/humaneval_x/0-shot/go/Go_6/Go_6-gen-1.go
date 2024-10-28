```go
func ParseNestedParens(paren_string string) []int {
    var max_levels []int
    groups := strings.Split(paren_string, " ")
    for _, group := range groups {
        depth := 0
        max_level := 0
        for _, c := range group {
            if c == '(' {
                depth++
                if depth > max_level {
                    max_level = depth
                }
            } else if c == ')' {
                depth--
            }
        }
        max_levels = append(max_levels, max_level)
    }
    return max_levels
}
```
