    str = strings.ToLower(str)
    count := 0
    m := make(map[rune]bool)

    for _, char := range str {
        if _, ok := m[char]; !ok {
            m[char] = true
            count++
        }
    }

    return count
}



