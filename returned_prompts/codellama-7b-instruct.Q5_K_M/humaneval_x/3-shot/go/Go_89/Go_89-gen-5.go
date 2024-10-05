    var result strings.Builder
    var offset int = 2 * 2
    for _, r := range s {
        if r >= 'a' && r <= 'z' {
            result.WriteRune('a' + (r - 'a' + offset) % 26)
        } else if r >= 'A' && r <= 'Z' {
            result.WriteRune('A' + (r - 'A' + offset) % 26)
        } else {
            result.WriteRune(r)
        }
    }
    return result.String()
}



