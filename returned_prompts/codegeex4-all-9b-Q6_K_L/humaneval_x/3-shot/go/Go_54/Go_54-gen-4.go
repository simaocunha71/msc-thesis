    if len(s0) != len(s1) {
        return false
    }
    count := make(map[rune]int)

    for _, c := range s0 {
        count[c]++
    }

    for _, c := range s1 {
        if count[c] == 0 {
            return false
        }
        count[c]--
    }
    return true
}



