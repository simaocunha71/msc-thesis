    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }
    if len(strings.Split(parts[0], "")[1:]) > 3 {
        return "No"
    }
    if !strings.ContainsAny(parts[0], "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return "No"
    }
    if !strings.HasSuffix(parts[1], "txt") && !strings.HasSuffix(parts[1], "exe") && !strings.HasSuffix(parts[1], "dll") {
        return "No"
    }
    return "Yes"
}