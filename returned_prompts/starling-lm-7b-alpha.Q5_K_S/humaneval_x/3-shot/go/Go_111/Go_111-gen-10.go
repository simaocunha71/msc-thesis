    result := make(map[rune]int)
    test = strings.ToLower(test)
    for _, char := range test {
        result[char] += 1
    }
    return result
}



