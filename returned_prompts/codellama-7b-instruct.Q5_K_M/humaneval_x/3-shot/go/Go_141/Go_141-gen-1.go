    if len(file_name) > 3 {
        return "No"
    }

    if !strings.Contains(file_name, ".") || len(strings.Split(file_name, ".")) != 2 {
        return "No"
    }

    if file_name[0] < 'A' || file_name[0] > 'Z' {
        return "No"
    }

    if !strings.Contains(file_name, "txt") || !strings.Contains(file_name, "exe") || !strings.Contains(file_name, "dll") {
        return "No"
    }

    return "Yes"
}



