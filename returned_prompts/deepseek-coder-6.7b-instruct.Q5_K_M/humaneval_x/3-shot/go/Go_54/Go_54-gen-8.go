    chars0 := make(map[rune]int)
    chars1 := make(map[rune]int)

    for _, c := range s0 {
        chars0[c]++
    }

    for _, c := range s1 {
        chars1[c]++
    }

    if len(chars0) != len(chars1) {
        return false
    }

    for c, count := range chars0 {
        if chars1[c] != count {
            return false
        }
    }

    return true
}



