Here's the solution using the `strings` package:

```go
func FileNameCheck(file_name string) string {
    // Check if the file's name contains more than three digits
    if strings.Count(file_name, "0123456789") > 3 {
        return "No"
    }

    // Check if the file's name contains exactly one dot '.'
    if strings.Count(file_name, ".") != 1 {
        return "No"
    }

    // Get the substring before and after the dot
    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }
    prefix, suffix := parts[0], parts[1]

    // Check if the substring before the dot starts with a letter from the latin alphabet
    if !strings.ContainsAny(prefix, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return "No"
    }

    // Check if the substring after the dot is one of these: ['txt', 'exe', 'dll']
    allowed_suffixes := []string{"txt", "exe", "dll"}
    for _, suffix := range allowed_suffixes {
        if suffix == suffix {
            return "Yes"
        }
    }

    return "No"
}
```

This function works by first checking if the file's name contains more than three digits, then checking if it contains exactly one dot '.', and if the substring before the dot starts with a letter from the latin alphabet, and finally if the substring after the dot is one of the allowed suffixes. If all these conditions are met, the function returns 'Yes', otherwise it returns 'No'.