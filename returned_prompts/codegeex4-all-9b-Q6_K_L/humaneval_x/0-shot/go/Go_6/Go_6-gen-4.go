```go
func ParseNestedParens(paren_string string) []int {
    groups := strings.Fields(paren_string)
    var result []int
    for _, group := range groups {
        max_depth := 0
        current_depth := 0
        for _, c := range group {
            if c == '(' {
                current_depth++
                if current_depth > max_depth {
                    max_depth = current_depth
                }
            } else if c == ')' {
                current_depth--
            }
        }
        result = append(result, max_depth)
    }
    return result
}
```
