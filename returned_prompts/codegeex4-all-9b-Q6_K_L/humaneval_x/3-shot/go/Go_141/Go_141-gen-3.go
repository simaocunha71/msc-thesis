    if len(file_name) < 5 {
        return "No"
    }

    for _, c := range file_name {
        if c >= '0' && c <= '9' {
            if len(file_name) - strings.Index(file_name, ".") - 1 > 3 {
                return "No"
            }
        }
    }

    if strings.Index(file_name, ".") == -1 {
        return "No"
    } else if strings.Index(file_name, ".") == len(file_name) - 1 {
        return "No"
    } else if strings.Index(file_name, ".") == 0 {
        return "No"
    } else if !strings.ContainsRune("abcdefghijklmnopqrstuvwxyz", rune(file_name[0])) && !strings.ContainsRune("ABCDEFGHIJKLMNOPQRSTUVWXYZ", rune(file_name[0])) {
        return "No"
    } else if strings.Index(file_name, ".") != len(file_name) - 4 {
        return "No"
    } else if !strings.HasSuffix(file_name, ".txt") && !strings.HasSuffix(file_name, ".exe") && !strings.HasSuffix(file_name, ".dll") {
        return "No"
    }

    return "Yes"
}

