    if strings.Count(file_name, ".") != 1 {
        return "No"
    }
    parts := strings.Split(file_name, ".")
    if len(parts[0]) == 0 {
        return "No"
    }
    if len(parts[0]) > 3 {
        return "No"
    }
    if !((parts[0][0] >= 'a' && parts[0][0] <= 'z') || (parts[0][0] >= 'A' && parts[0][0] <= 'Z')) {
        return "No"
    }
    if parts[1] != "txt" && parts[1] != "exe" && parts[1] != "dll" {
        return "No"
    }
    return "Yes"
}



