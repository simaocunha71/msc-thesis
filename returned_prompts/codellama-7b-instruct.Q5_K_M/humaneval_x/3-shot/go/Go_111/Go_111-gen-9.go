    result := make(map[rune]int)
    for _, c := range strings.Fields(test) {
        if _, ok := result[rune(c)]; ok {
            result[rune(c)] += 1
        } else {
            result[rune(c)] = 1
        }
    }
    return result
}



