```go
func ParseNestedParens(paren_string string) []int {
    groups := strings.Split(paren_string, " ")
    result := make([]int, 0, len(groups))

    for _, group := range groups {
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
        result = append(result, max_depth)
    }

    return result
}
```