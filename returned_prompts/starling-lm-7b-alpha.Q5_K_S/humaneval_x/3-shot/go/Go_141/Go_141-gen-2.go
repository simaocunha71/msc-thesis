    var result = "No"
    var letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if len(file_name) > 3 {
        return result
    }
    if strings.Count(file_name, ".") != 1 {
        return result
    }

    var parts = strings.Split(file_name, ".")
    if len(parts) != 2 {
        return result
    }
    if len(parts[0]) == 0 {
        return result
    }
    if !strings.ContainsRune(letters, rune(parts[0][0])) {
        return result
    }

    if parts[1] == "txt" || parts[1] == "exe" || parts[1] == "dll" {
        result = "Yes"
    }
    return result
}



