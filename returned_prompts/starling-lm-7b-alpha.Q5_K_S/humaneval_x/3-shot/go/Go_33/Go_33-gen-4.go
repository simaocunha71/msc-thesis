    result := make([]int, len(l))
    for i := 0; i < len(l); i++ {
        if i % 3 == 0 {
            result[i] = l[sort.SearchInts(l, l[i])]
        }else {
            result[i] = l[i]
        }
    }
    return result
}



