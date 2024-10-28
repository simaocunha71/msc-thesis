    result := make([]int, len(l))
    for i, v := range l {
        if i%2 == 0 {
            result[i] = v
        } else {
            result[i] = v
            sort.Ints(result[i:])
        }
    }
    return result
}



