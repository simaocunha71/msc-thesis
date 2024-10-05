    parts := strings.split(file_name, '.')
    if len(parts) != 2 {
        return "No"
    }
    name, ext := parts[0], parts[1]
    if len(name) == 0 || !name[0].IsLetter() {
        return "No"
    }
    count := 0
    for _, ch := range name {
        if ch.IsDigit() {
            count += 1
        }
    }
    if count > 3 {
        return "No"
    }
    if ext != 'txt' && ext != 'exe' && ext != 'dll' {
        return "No"
    }
    return "Yes"
}



