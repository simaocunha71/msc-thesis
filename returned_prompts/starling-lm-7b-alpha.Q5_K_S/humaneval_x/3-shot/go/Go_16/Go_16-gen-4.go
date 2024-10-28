    result := make(map[rune]struct{}, 0)
    for _, c := range str {
        result[c] = struct{}{}
    }
    return len(result)
}



