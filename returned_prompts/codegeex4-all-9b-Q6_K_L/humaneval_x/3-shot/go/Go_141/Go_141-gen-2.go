    var result string = "No"
    var digits int = 0
    var dot_count int = 0

    for _, c := range file_name {
        if c >= '0' && c <= '9' {
            digits += 1
        } else if c == '.' {
            dot_count += 1
        }
    }

    if dot_count == 1 && digits <= 3 {
        parts := strings.Split(file_name, ".")
        if len(parts[0]) > 0 && (parts[1] == "txt" || parts[1] == "exe" || parts[1] == "dll") {
            for _, c := range parts[0] {
                if !((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
                    return result
                }
            }
            result = "Yes"
        }
    }

    return result
}

