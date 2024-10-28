```go
func ParseNestedParens(paren_string string) []int {
    levels := strings.Fields(paren_string)
    result := make([]int, 0, len(levels))
    for _, level := range levels {
        max_depth := 0
        depth := 0
        for _, c := range level {
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
