    if len(file_name) > 3 {
        return "No"
    }
    if !strings.Contains(file_name, ".") {
        return "No"
    }
    if len(strings.Split(file_name, ".")[0]) == 0 {
        return "No"
    }
    if !(strings.Split(file_name, ".")[1] == "txt" || strings.Split(file_name, ".")[1] == "exe" || strings.Split(file_name, ".")[1] == "dll") {
        return "No"
    }
    return "Yes"
}



