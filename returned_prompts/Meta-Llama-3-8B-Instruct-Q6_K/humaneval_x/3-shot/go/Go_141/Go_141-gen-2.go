    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }
    if len(parts[0]) == 0 || !strings.ContainsAny(parts[0], "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return "No"
    }
    if len(parts[1]) > 3 {
        return "No"
    }
    if !strings.Contains([]string{"txt", "exe", "dll"}, parts[1]) {
        return "No"
    }
    return "Yes"
}