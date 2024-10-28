```go
func ParseNestedParens(paren_string string) []int {
    paren_groups := strings.Split(paren_string, " ")
    max_depths := make([]int, len(paren_groups))
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
        max_depths[i] = max_depth
    }
    return max_depths
}
```
