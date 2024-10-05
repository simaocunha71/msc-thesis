    if len(file_name) == 0 {
        return "No"
    }

B:
    count := strings.Count(file_name, ".")
    if count != 1 {
        return "No"
    }

C:
    dot_index := strings.Index(file_name, ".")
    if !(strings.Index('a', file_name[:dot_index]) && strings.Index('z', file_name[:dot_index]) || strings.Index('A', file_name[:dot_index]) && strings.Index('Z', file_name[:dot_index])) {
        return "No"
    }

D:
    post_dot := file_name[dot_index+1:]
    if !(post_dot == "txt" || post_dot == "exe" || post_dot == "dll") {
        return "No"
    }

E:
    digit_count := 0
    for _, c := range file_name {
        if '0' <= c && c <= '9' {
            digit_count++
        }
    }

    if digit_count > 3 {
        return "No"
    }

F:
    return "Yes"
}

```

It seems like you're asking for a solution in Go programming language. However, the code you provided seems to have some syntax errors. Let's fix those and rewrite the function:

```go
