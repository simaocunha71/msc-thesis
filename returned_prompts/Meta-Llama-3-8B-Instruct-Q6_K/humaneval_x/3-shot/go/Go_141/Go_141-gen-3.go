    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }
    if !strings.HasPrefix(parts[0], "a-zA-Z") {
        return "No"
    }
    if len(strings.Replace(parts[0], "a-zA-Z", "", -1)) > 0 {
        return "No"
    }
    if len(strings.Replace(parts[1], "txtexe.dll", "", -1)) > 0 {
        return "No"
    }
    if len(strings.Count(file_name, "0-9")) > 3 {
        return "No"
    }
    return "Yes"
}  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3.1.4.1.1  // 3