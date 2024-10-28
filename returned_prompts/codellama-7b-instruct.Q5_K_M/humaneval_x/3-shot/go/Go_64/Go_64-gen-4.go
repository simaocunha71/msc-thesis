    vowels := []string{"a", "e", "i", "o", "u", "y"}
    count := 0
    for _, c := range s {
        if strings.Contains(strings.ToLower(string(c)), string(c)) {
            count += 1
        }
    }
    return count
}



