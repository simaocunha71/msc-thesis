    if len(s0) != len(s1) {
        return false
    }

    charMap := make(map[rune]int)
    for _, c := range s0 {
        charMap[c]++
    }

    for _, c := range s1 {
        charMap[c]--
        if charMap[c] < 0 {
            return false
        }
    }

    return true
}