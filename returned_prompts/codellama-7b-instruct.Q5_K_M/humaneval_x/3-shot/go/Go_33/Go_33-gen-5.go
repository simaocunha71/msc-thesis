    result := make([]int, len(l))
    for i, v := range l {
        if i%3 == 0 {
            result[i] = v
        } else {
            result[i] = l[i-1]
        }
    }
    sort.Ints(result)
    return result
}



