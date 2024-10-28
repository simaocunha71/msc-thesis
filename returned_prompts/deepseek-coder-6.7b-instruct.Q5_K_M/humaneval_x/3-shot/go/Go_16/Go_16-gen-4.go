    str = strings.ToLower(str)
    counter := make(map[rune]int)
    for _, char := range str {
        counter[char]++
    }

    return len(counter)
}



