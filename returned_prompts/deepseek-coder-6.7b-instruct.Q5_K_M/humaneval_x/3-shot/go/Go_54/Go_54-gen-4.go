    charCount := make(map[rune]int)

    for _, c := range s0 {
        charCount[c]++
    }

    for _, c := range s1 {
        if _, ok := charCount[c]; !ok {
            return false
        }
        charCount[c]--
        if charCount[c] < 0 {
            return false
        }
    }

    return true
}



