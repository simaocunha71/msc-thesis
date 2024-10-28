    result := make([]int, 0)
    for i, v := range l {
        if i%3 == 0 {
            result = append(result, sort.Ints(l[i:i+1])...)
        } else {
            result = append(result, v)
        }
    }
    return result
}