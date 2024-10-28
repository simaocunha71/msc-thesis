    str = strings.ToLower(str)
    count := make(map[rune]int)
    for _, c := range str {
        count[c] += 1
    }
    return len(count)
}



