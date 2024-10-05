    vowels := "aeiouy"
    count := 0
    for _, c := range strings.ToLower(s) {
        if strings.Contains(vowels, string(c)) {
            count += 1
        }
    }
    return count
}



