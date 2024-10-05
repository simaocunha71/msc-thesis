    result := make(map[rune]int)

    for _, r := range test {
        if strings.ContainsRune("abcdefghijklmnopqrstuvwxyz", r) {
            result[r] += 1
        }
    }
    return result
}



