    if len(file_name) > 3 {
        return "No"
    }
    if !strings.Contains(file_name, ".") {
        return "No"
    }
    if len(strings.Split(file_name, ".")[0]) == 0 {
        return "No"
    }
    if !strings.HasPrefix(strings.Split(file_name, ".")[0], "a") && !strings.HasPrefix(strings.Split(file_name, ".")[0], "A") &&
        !strings.HasPrefix(strings.Split(file_name, ".")[0], "b") && !strings.HasPrefix(strings.Split(file_name, ".")[0], "B") &&
        !strings.HasPrefix(strings.Split(file_name, ".")[0], "c") && !strings.HasPrefix(strings.Split(file_name, ".")[0], "C") &&
        !strings.HasPrefix(strings.Split(file_name, ".")[0], "d") && !strings.HasPrefix(strings.Split(file_name, ".")[0], "D") &&
        !strings.HasPrefix(strings.Split(file_name, ".")[0], "e") && !strings.HasPrefix(strings.Split(file_name, ".")[0], "E") &&
        !strings.HasPrefix(strings.Split(file_name, ".")[0], "f") && !strings.HasPrefix(strings.Split(file_name, ".")[0], "F") &&
        !strings.HasPrefix(strings.Split(file_name, ".")[0], "g") && !strings.HasPrefix(strings.Split(file_name, ".")[0], "G") &&
        !strings.HasPrefix(strings.Split(file_name, ".")[0], "h") && !strings.HasPrefix(strings.Split(file_name, ".")[0], "H") &&
        !strings.HasPrefix(strings.Split(file_name, ".")[0], "i") && !strings.HasPrefix(strings.Split(file_name, ".")[0], "I") &&
        !