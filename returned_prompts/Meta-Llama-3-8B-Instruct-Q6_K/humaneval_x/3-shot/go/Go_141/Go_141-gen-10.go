    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }
    if !strings.Contains(parts[0], `[a-zA-Z]`) {
        return "No"
    }
    if len(strings.Replace(parts[0], `[a-zA-Z]`, "", -1)) > 0 {
        return "No"
    }
    if len(strings.Replace(parts[1], "txt", "", -1)) > 0 && len(strings.Replace(parts[1], "exe", "", -1)) > 0 && len(strings.Replace(parts[1], "dll", "", -1)) > 0 {
        return "No"
    }
    if len(strings.Replace(parts[1], "txt", "", -1)) > 0 && len(strings.Count(parts[1], "exe")) > 3 {
        return "No"
    }
    return "Yes"
}
}}



