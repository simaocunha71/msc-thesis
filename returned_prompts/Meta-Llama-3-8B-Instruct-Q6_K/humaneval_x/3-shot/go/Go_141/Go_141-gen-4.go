    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }
    if len(strings.Replace(parts[0], ".", "", -1)) > 0 && !strings.Contains(parts[0], "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return "No"
    }
    if len(strings.Replace(parts[1], ".", "", -1)) > 3 {
        return "No"
    }
    if parts[1] != "txt" && parts[1] != "exe" && parts[1] != "dll" {
        return "No"
    }
    return "Yes"
}