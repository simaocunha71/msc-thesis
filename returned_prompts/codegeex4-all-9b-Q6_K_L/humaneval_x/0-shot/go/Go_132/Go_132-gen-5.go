```go
func IsNested(s string) bool {
    left := []int{}
    for i := 0; i < len(s); i++ {
        if s[i] == '[' {
            left = append(left, i)
        } else if s[i] == ']' {
            if len(left) > 0 {
                left = left[:len(left)-1]
            } else {
                return true
            }
        }
    }
    return len(left) > 0
}
```
