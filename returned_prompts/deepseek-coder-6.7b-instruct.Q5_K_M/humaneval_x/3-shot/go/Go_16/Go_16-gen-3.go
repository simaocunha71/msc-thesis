    str = strings.ToLower(str)
    count := 0
    exist := make(map[rune]bool)

    for _, c := range str {
        if _, ok := exist[c]; !ok {
            exist[c] = true
            count++
        }
    }
    return count
}



