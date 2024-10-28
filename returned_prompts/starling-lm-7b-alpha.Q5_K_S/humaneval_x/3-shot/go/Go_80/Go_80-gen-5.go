    if len(s) < 3 {
        return false
    }

    happy_set := make(map[rune]bool)

    for i := 0; i < len(s)-2; i++ {
        r1, r2, r3 := s[i], s[i+1], s[i+2]
        happy_set[r1] = true
        if happy_set[r2] {
            return false
        }
        happy_set[r2] = true
        if happy_set[r3] {
            return false
        }
        happy_set[r3] = true
    }
    return true
}



