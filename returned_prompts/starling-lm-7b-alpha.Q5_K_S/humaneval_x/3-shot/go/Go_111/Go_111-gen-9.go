    result := make(map[rune]int)
    for _, char := range test {
        result[char]++
    }
    return result
}



