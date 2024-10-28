    count := 0
    for i, v := range s {
        if i%2 == 0 {
            if strings.ContainsRune("AEIOU", v) {
                count++
            }
        }
    }
    return count
}

