```go
func FileNameCheck(file_name string) string {
    n_digits := 0
    n_dots := 0
    before_dot := ""
    after_dot := ""

    for _, c := range file_name {
        if c >= '0' && c <= '9' {
            n_digits++
        } else if c == '.' {
            n_dots++
            if before_dot == "" {
                return "No"
            }
        } else if n_dots == 0 {
            before_dot += string(c)
        } else if after_dot == "" {
            after_dot = string(c)
        } else {
            return "No"
        }
    }

    if n_digits > 3 || n_dots != 1 || !strings.Contains("txtexe.dll", after_dot) {
        return "No"
    }

    if before_dot == "" || !((before_dot[0] >= 'a' && before_dot[0] <= 'z') || (before_dot[0] >= 'A' && before_dot[0] <= 'Z')) {
        return "No"
    }

    return "Yes"
}
```
