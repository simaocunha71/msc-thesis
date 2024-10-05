```go
func ParseNestedParens(paren_string string) []int {
    paren_groups := strings.Fields(paren_string)
    result := make([]int, len(paren_groups))
    for i, group := range paren_groups {
        depth := 0
        max_depth := 0
        for _, c := range group {
            if c == '(' {
                depth++
                if depth > max_depth {
                    max_depth = depth
                }
            } else if c == ')' {
                depth--
            }
        }
        result[i] = max_depth
    }
    return result
}
```