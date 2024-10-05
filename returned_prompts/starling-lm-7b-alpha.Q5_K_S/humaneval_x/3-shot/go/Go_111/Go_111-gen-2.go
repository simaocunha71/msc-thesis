    result := make(map[rune]int)
    for _, c := range test {
        result[c]++
    }
    return result
}



