    str = strings.ToLower(str)
    count := 0
    for _, char := range str {
        r := []rune(str)
        if len(r) == count(r) {
            count++
        }
    }
    return count
}



