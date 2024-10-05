    name := strings.Fields(file_name)

    if len(name) != 2 {
        return "No"
    }

    if len(name[0]) == 0 {
        return "No"
    }

    if len(name[1]) != 3 || name[1][0] != '.' {
        return "No"
    }

    if !strings.ContainsAny(name[0], "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return "No"
    }

    if name[1] != "txt" && name[1] != "exe" && name[1] != "dll" {
        return "No"
    }

    return "Yes"
}



