    var count int = 0

    for _, c := range s {
        if strings.Contains("a", string(c)) || strings.Contains("e", string(c)) || strings.Contains("i", string(c)) || strings.Contains("o", string(c)) || strings.Contains("u", string(c)) || strings.Contains("y", string(c)) {
            count += 1
        }
    }
    return count
}



