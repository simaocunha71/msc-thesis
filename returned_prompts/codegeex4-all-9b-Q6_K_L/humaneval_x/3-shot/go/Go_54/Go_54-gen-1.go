    var m = make(map[rune]int)
    for _, c := range s0 {
        m[c]++
    }

    for _, c := range s1 {
        if _, exists := m[c]; !exists {
            return false
        }
        m[c]--
        if m[c] < 0 {
            return false
        }
    }
    return true
}



