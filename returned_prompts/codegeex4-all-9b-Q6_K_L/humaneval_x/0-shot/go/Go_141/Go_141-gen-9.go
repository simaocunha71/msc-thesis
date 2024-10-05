```go
func FileNameCheck(file_name string) string {
    if len(strings.FieldsFunc(file_name, func(r rune) bool {
        return unicode.IsDigit(r)
    })) > 3 {
        return "No"
    }
    if strings.Count(file_name, ".") != 1 {
        return "No"
    }
    name, ext := strings.Split(file_name, ".")[0], strings.Split(file_name, ".")[1]
    if len(name) == 0 || !unicode.IsLetter(rune(name[0])) {
        return "No"
    }
    if !strings.ContainsAny(ext, "txtexedll") {
        return "No"
    }
    return "Yes"
}
```