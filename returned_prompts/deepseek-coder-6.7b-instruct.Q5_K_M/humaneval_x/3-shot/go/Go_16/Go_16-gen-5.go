    str = strings.ToLower(str)
    countMap := make(map[rune]bool)
    for _, char := range str {
        countMap[char] = true
    }

    return len(countMap)
}



