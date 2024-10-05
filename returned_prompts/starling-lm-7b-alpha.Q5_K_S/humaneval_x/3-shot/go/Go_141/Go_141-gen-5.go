    if len(file_name) < 1 {
        return "No"
    }
    if len(file_name) > 4 {
        return "No"
    }

    for i, c := range file_name {
        if i == 0 && (c < 'a' || c > 'z' || c < 'A' || c > 'Z') {
            return "No"
        }
        if i > 0 && c < '0' || c > '9' {
            return "No"
        }
    }
    if file_name[len(file_name)-1] == '.' {
        return "No"
    }
    if !strings.HasSuffix(file_name, ".txt") &&
       !strings.HasSuffix(file_name, ".exe") &&
       !strings.HasSuffix(file_name, ".dll") {
           return "No"
    }
    return "Yes"
}



