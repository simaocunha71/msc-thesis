    if len(file_name) < 3 || len(file_name) > 10 {
        return "No"
    }
    name_parts := strings.Split(file_name, ".")
    if len(name_parts) != 2 {
        return "No"
    }
    if name_parts[0] == "" {
        return "No"
    }
    if name_parts[1] != "txt" && name_parts[1] != "exe" && name_parts[1] != "dll" {
        return "No"
    }
    if !strings.HasPrefix(name_parts[0], string(rune(97)) ) && !strings.HasPrefix(name_parts[0], string(rune(65)) ){
        return "No"
    }

    return "Yes"
}



