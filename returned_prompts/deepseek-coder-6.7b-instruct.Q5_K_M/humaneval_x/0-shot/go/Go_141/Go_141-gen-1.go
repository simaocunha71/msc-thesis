    if len(file_name) == 0 {
        return "No"
    }

B:
    if strings.Count(file_name, ".") > 1 {
        return "No"
    }

C:
    split := strings.Split(file_name, ".")
    if len(split) != 2 {
        return "No"
    }

D:
    if len(split[0]) == 0 {
        return "No"
    }

E:
    if !((split[0][0] >= 'a' && split[0][0] <= 'z') || (split[0][0] >= 'A' && split[0][0] <= 'Z')) {
        return "No"
    }

F:
    if strings.ContainsAny(split[0], "0123456789") {
        return "No"
    }

G:
    if strings.Count(split[0], "") > 3 {
        return "No"
    }

H:
    if split[1] != "txt" && split[1] != "exe" && split[1] != "dll" {
        return "No"
    }

I:
    return "Yes"
}
```

## 2.1
```go
