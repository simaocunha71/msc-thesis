    if len(file_name) > 4 {
        return "No"
    }

    if strings.Count(file_name, ".") != 1 {
        return "No"
    }

    if strings.Count(file_name, "0123456789") > 3 {
        return "No"
    }

    if !strings.HasPrefix(file_name[:strings.Index(file_name, ".")], "") {
        return "No"
    }

    if !strings.Contains(file_name, ".") {
        return "No"
    }

    if strings.HasSuffix(file_name, ".txt") || strings.HasSuffix(file_name, ".exe") || strings.HasSuffix(file_name, ".dll") {
        return "Yes"
    }else {
        return "No"
    }
}



