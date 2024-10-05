    if len(s0) != len(s1) {
        return false
    }
    count0 := make(map[rune]int)
    count1 := make(map[rune]int)
    for _, c := range s0 {
        count0[c]++
    }
    for _, c := range s1 {
        count1[c]++
    }
    for k, v := range count0 {
        if v != count1[k] {
            return false
        }
    }
    return true
}