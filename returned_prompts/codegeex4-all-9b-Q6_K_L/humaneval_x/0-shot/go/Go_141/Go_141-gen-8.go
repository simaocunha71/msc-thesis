```go
func FileNameCheck(file_name string) string {
    // Check if the file name has more than three digits
    if strings.Count(file_name, "0123456789") > 3 {
        return "No"
    }

    // Check if the file name contains exactly one dot '.'
    if strings.Count(file_name, ".") != 1 {
        return "No"
    }

    // Split the file name into two parts: name and extension
    parts := strings.Split(file_name, ".")
    name := parts[0]
    extension := parts[1]

    // Check if the name starts with a latin alphabet letter and does not contain digits
    if !strings.HasPrefix(name, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") || strings.ContainsAny(name, "0123456789") {
        return "No"
    }

    // Check if the extension is one of the allowed types
    if extension != "txt" && extension != "exe" && extension != "dll" {
        return "No"
    }

    return "Yes"
}
```