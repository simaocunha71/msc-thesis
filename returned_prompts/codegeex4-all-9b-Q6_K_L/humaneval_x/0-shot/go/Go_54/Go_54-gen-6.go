// count characters in string 0
    m := make(map[rune]int)
    for _, c := range s0 {
        m[c]++
    }

    // check that string 1 has same characters
    for _, c := range s1 {
        m[c]--
        if m[c] < 0 {
            return false
        }
    }
    return true
}