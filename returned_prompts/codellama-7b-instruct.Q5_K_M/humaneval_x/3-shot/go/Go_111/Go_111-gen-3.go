    letter_count := make(map[rune]int)
    for _, c := range test {
        if strings.ContainsAny(string(c), "abcdefghijklmnopqrstuvwxyz") {
            letter_count[c] += 1
        }
    }
    return letter_count
}



