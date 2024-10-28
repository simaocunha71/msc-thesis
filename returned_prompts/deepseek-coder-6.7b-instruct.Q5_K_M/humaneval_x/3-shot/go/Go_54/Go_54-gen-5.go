    charMap := map[rune]int{}

    for _, c := range s0 {
        charMap[c]++
    }

    for _, c := range s1 {
        if _, ok := charMap[c]; !ok {
            return false
        }
        charMap[c]--
        if charMap[c] < 0 {
            return false
        }
    }

    return true
}



