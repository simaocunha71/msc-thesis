    distinct := map[int]int{}

    for _, v := range l {
        if _, ok := distinct[v]; ok {
            return true
        }
        if _, ok := distinct[-v]; ok {
            return true
        }
        distinct[v] = 1
    }

    return false
}



