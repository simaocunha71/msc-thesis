    s0_map := make(map[rune]int)
    for _, c := range s0 {
        s0_map[c] += 1
    }

    s1_map := make(map[rune]int)
    for _, c := range s1 {
        s1_map[c] += 1
    }

    return s0_map == s1_map
}



