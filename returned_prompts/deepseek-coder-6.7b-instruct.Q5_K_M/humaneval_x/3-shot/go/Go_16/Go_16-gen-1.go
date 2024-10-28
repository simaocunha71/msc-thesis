    count := make(map[rune]int)
    for _, c := range strings.ToLower(str) {
        count[c]++
    }
    return len(count)
}

