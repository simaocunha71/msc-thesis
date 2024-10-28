    result := make([]rune, 0)

    for _, c := range s {
        if (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') {
            if c >= 'a' {
                result = append(result, c - 32)
            } else {
                result = append(result, c + 32)
            }
        } else {
            result = append(result, c)
        }
    }

    if len(result) > 0 {
        return string(result)
    } else {
        return ""
    }

}