```go
func CorrectBracketing(brackets string) bool {
    count := 0
    for _, b := range brackets {
        if b == '(' {
            count++
        } else if b == ')' {
            count--
        }
        if count < 0 {
            return false
        }
    }
    return count == 0
}
```

