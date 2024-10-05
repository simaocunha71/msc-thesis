    result := make(map[rune]int)
    for _, c := range test {
        result[c] += 1
    }
    return result
}



