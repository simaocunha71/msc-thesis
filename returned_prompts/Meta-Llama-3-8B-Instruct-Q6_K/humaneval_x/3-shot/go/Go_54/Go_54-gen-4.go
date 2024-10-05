    if len(s0) != len(s1) {
        return false
    }
    map0 := make(map[rune]int)
    map1 := make(map[rune]int)
    for _, c := range s0 {
        map0[c]++
    }
    for _, c := range s1 {
        map1[c]++
    }
    for k, v := range map0 {
        if v != map1[k] {
            return false
        }
    }
    return true
}