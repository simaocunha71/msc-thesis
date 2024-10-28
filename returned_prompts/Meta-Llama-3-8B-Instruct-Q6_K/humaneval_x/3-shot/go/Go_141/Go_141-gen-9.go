    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }
    if !strings.HasPrefix(parts[0], string(rune('a'))+string(rune('z'))+string(rune('A'))+string(rune('Z'))) {
        return "No"
    }
    if len(strings.Replace(parts[0], string(rune('a'))+string(rune('z'))+string(rune('A'))+string(rune('Z')), "", -1)) > 0 {
        return "No"
    }
    if len(strings.Replace(parts[1], "txt", "", -1)) > 0 && len(strings.Replace(parts[1], "exe", "", -1)) > 0 && len(strings.Replace(parts[1], "dll", "", -1)) > 0 {
        return "No"
    }
    for _, c := range parts[1] {
        if c >= '0' && c <= '9' {
            if len(strings.Replace(parts[1], string(rune('0'))+string(rune('9')), "", -1)) > 3 {
                return "No"
            }
        }
    }
    return "Yes"
}