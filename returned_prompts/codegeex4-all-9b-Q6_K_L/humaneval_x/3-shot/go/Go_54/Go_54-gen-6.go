    count := make(map[rune]int)

    for _, c := range s0 {
        count[c]++
    }

    for _, c := range s1 {
        count[c]--
        if count[c] < 0 {
            return false
        }
    }

    for _, v := range count {
        if v != 0 {
            return false
        }
    }

    return true
}

