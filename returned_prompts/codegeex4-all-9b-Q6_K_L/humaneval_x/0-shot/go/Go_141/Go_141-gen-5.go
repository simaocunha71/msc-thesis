```go
func FileNameCheck(file_name string) string {
    if !strings.Contains(file_name, ".") {
        return "No"
    }
    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }
    if !strings.HasPrefix(parts[0], strings.ToLower(string(parts[0][0]))) {
        return "No"
    }
    if len(parts[0]) > 3 && strings.Count(parts[0], "0123456789") > 3 {
        return "No"
    }
    if !contains(parts[1], []string{"txt", "exe", "dll"}) {
        return "No"
    }
    return "Yes"
}

func contains(s string, l []string) bool {
    for _, i := range l {
        if i == s {
            return true
        }
    }
    return false
}
```
