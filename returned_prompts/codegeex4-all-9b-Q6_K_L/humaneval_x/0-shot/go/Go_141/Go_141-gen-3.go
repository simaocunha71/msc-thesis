```go
func FileNameCheck(file_name string) string {
    if len(file_name) == 0 {
        return "No"
    }

    dot_count := strings.Count(file_name, ".")
    if dot_count != 1 {
        return "No"
    }

    parts := strings.Split(file_name, ".")
    if len(parts[0]) == 0 || len(parts[1]) == 0 {
        return "No"
    }

    if !('a' <= parts[0][0] && parts[0][0] <= 'z' || 'A' <= parts[0][0] && parts[0][0] <= 'Z') {
        return "No"
    }

    if parts[1] != "txt" && parts[1] != "exe" && parts[1] != "dll" {
        return "No"
    }

    digit_count := 0
    for _, c := range parts[0] {
        if '0' <= c && c <= '9' {
            digit_count++
            if digit_count > 3 {
                return "No"
            }
        }
    }

    return "Yes"
}
```