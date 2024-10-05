    if len(s0) != len(s1)  {
        return false
    }

    charCounts0 := make(map[rune]int)
    charCounts1 := make(map[rune]int)

    for _, c := range s0  {
        charCounts0[c] += 1
    }

    for _, c := range s1  {
        charCounts1[c] += 1
    }

    for k, v := range charCounts0  {
        if charCounts1[k] != v  {
            return false
        }
    }

    return true
}



