    charset := make(map[rune]struct{})
    for _,c := range str {
        charset[c] = struct{}{}
    }
    return len(charset)
}



