    result := make([]int, len(l))
    for i := 0; i < len(l); i++ {
        if i % 3 == 0 {
            sort.Ints(l[i:i+3])
            result[i] = l[i+2]
        } else {
            result[i] = l[i]
        }
    }
    return result
}



