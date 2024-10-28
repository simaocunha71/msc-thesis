    var count int = 0
    for _, c := range strings.ToLower(s) {
        if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y' {
            count += 1
        }
    }
    return count
}



