    words := strings.Split(s," ")
    r := make([]rune, 0)
    for _, word := range words {
        r = append(r, rune(word))
        for _, char := range word {
            r = append(r, char)
            r = append(r, rune(sort.IntSlice([]int{int(char)}).Slice()))
        }
    }
    return string(r)
}



