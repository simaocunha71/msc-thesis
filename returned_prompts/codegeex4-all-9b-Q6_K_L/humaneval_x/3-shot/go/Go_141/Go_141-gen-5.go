    if strings.Count(file_name, ".") != 1 {
        return "No"
    }

    parts := strings.Split(file_name, ".")
    if len(parts[0]) == 0 || len(parts[0]) > 3 {
        return "No"
    }

    if parts[1] != "txt" && parts[1] != "exe" && parts[1] != "dll" {
        return "No"
    }

    if !strings.ContainsAny(parts[0], "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return "No"
    }

    return "Yes"
}



