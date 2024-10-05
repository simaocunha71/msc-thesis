```go
func FileNameCheck(file_name string) string {
    if strings.Count(file_name, ".") != 1 {
        return "No"
    }
    name, ext := strings.Split(file_name, ".")[0], strings.Split(file_name, ".")[1]
    if !strings.HasPrefix(name, "a") && !strings.HasPrefix(name, "A") {
        return "No"
    }
    if !strings.ContainsAny(name, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return "No"
    }
    if len(name) > 3 && !strings.HasPrefix(name[3:], "0") && !strings.HasPrefix(name[3:], "1") && !strings.HasPrefix(name[3:], "2") && !strings.HasPrefix(name[3:], "3") && !strings.HasPrefix(name[3:], "4") && !strings.HasPrefix(name[3:], "5") && !strings.HasPrefix(name[3:], "6") && !strings.HasPrefix(name[3:], "7") && !strings.HasPrefix(name[3:], "8") && !strings.HasPrefix(name[3:], "9") {
        return "No"
    }
    if ext != "txt" && ext != "exe" && ext != "dll" {
        return "No"
    }
    return "Yes"
}
```