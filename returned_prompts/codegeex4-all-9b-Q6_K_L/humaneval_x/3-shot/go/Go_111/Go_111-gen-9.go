    result := make(map[rune]int)
    for _, c := range strings.Split(test, " ") {
        if len(c) != 0 {
            result[rune(c[0])]++
        }
    }
    return result
}

