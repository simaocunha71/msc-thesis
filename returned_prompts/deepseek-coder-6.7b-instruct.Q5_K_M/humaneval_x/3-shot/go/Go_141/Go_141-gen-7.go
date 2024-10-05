    if strings.Count(file_name, ".") > 1 {
        return "No"
    }

    if !strings.Contains(file_name, ".") {
        return "No"
    }

    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }

    if !((parts[0][0] >= 'a' && parts[0][0] <= 'z') || (parts[0][0] >= 'A' && parts[0][0] <= 'Z')) {
        return "No"
    }

    if parts[0] == "" {
        return "No"
    }

    if !(strings.Contains(file_name, "txt") || strings.Contains(file_name, "exe") || strings.Contains(file_name, "dll")) {
        return "No"
    }

    if len(strings.Replace(parts[0], "", "", -1)) > 3 {
        return "No"
    }

    return "Yes"
}



