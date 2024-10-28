    if strings.Count(file_name, ".") != 1 {
        return "No"
    }
    split_name := strings.Split(file_name, ".")
    if len(split_name[0]) == 0 || len(split_name[1]) == 0 {
        return "No"
    }
    if len(strings.Split(split_name[0], "")) > 3 {
        return "No"
    }
    if !((split_name[0][0] >= 'a' && split_name[0][0] <= 'z') || (split_name[0][0] >= 'A' && split_name[0][0] <= 'Z')) {
        return "No"
    }
    if split_name[1] != "txt" && split_name[1] != "exe" && split_name[1] != "dll" {
        return "No"
    }

    return "Yes"
}
```

#### Code 2:
```go
