```go
func FileNameCheck(file_name string) string {
    if strings.Count(file_name, ".") != 1 {
        return "No"
    }
    parts := strings.Split(file_name, ".")
    if len(parts[0]) == 0 || len(parts[0]) > 3 {
        return "No"
    }
    for _, r := range parts[0] {
        if r < 'a' || r > 'z' && r < 'A' || r > 'Z' {
            return "No"
        }
    }
    if !strings.ContainsAny(parts[1], "txtexedll") {
        return "No"
    }
    if strings.Count(parts[0], "0123456789") > 3 {
        return "No"
    }
    return "Yes"
}
```