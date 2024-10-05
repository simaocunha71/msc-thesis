```go
func FileNameCheck(file_name string) string {
    dotIndex := strings.Index(file_name, ".")
    if dotIndex == -1 || dotIndex == 0 || dotIndex == len(file_name)-1 {
        return "No"
    }
    nameBeforeDot := file_name[:dotIndex]
    nameAfterDot := file_name[dotIndex+1:]
    if len(nameBeforeDot) == 0 || len(nameAfterDot) != 3 {
        return "No"
    }
    if !strings.ContainsAny(nameBeforeDot, "0123456789") || len(nameBeforeDot) > 3 {
        return "No"
    }
    if !strings.ContainsRune(nameBeforeDot, 'a') && !strings.ContainsRune(nameBeforeDot, 'A') && !strings.ContainsRune(nameBeforeDot, 'z') && !strings.ContainsRune(nameBeforeDot, 'Z') {
        return "No"
    }
    validExtensions := []string{"txt", "exe", "dll"}
    for _, ext := range validExtensions {
        if nameAfterDot == ext {
            return "Yes"
        }
    }
    return "No"
}
```