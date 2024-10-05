    set := make(map[int]int)
    for _, v := range l {
        if _, ok := set[v]; ok {
            return true
        }
        set[v]++
    }

    return false
}



