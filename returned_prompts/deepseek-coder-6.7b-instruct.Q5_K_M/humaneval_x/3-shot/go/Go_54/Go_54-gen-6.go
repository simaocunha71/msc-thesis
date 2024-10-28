    sort.Slice([]rune(s0), func(i int, j int) bool { return []rune(s0)[i] < []rune(s0)[j] })
    sort.Slice([]rune(s1), func(i int, j int) bool { return []rune(s1)[i] < []rune(s1)[j] })
    return s0 == s1
}



