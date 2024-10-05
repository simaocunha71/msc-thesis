```go
func ParseNestedParens(paren_string string) []int {
    groups := strings.Split(paren_string, " ")
    results := make([]int, 0, len(groups))
    for _, group := range groups {
        max_depth := 0
        depth := 0
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
        results = append(results, max_depth)
    }
    return results
}
```
