    if len(file_name) < 2 {
        return "No"
    }
    if !strings.Contains(file_name, ".") {
        return "No"
    }
    parts := strings.SplitN(file_name, ".", 2)
    if len(parts[0]) > 0 && !strings.Contains(parts[0], "_") && !strings.Contains(parts[0], " ") && !strings.Contains(parts[0], "-") {
        if len(parts[0]) > 0 && !strings.Contains(parts[0], "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
            return "No"
        }
    }
    if len(parts[1]) > 4 {
        return "No"
    }
    if parts[1] != "txt" && parts[1] != "exe" && parts[1] != "dll" {
        return "No"
    }
    count := 0
    for _, char := range parts[0] {
        if char >= '0' && char <= '9' {
            count++
        }
        if count > 3 {
            return "No"
        }
    }
    return "Yes"
}