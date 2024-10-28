    result := make(map[rune]int)
    count := make(map[rune]int)
    for _, c := range test {
        if _, ok := count[c]; !ok {
            result[c] = 0
        }
        count[c] += 1
    }
    return result
}



