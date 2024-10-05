    var map0  = make(map[rune]int)
    var map1  = make(map[rune]int)

    for _, c := range s0 {
        map0[c]++
    }

    for _, c := range s1 {
        map1[c]++
    }

    if len(map0) != len(map1) {
        return false
    }

    for k, v := range map0 {
        if map1[k] != v {
            return false
        }
    }

    return true
}



