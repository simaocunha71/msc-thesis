    result := make([]int, 0, len(l))
    for i, v := range l {
        if i%2 == 0 {
            result = append(result, sort.Ints(l[i/2:i/2+1])...)
        } else {
            result = append(result, v)
        }
    }
    return result
}