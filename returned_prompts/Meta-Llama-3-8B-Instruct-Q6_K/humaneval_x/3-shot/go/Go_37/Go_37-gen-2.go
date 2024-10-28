    result := make([]int, 0)
    for i, v := range l {
        if i % 2 == 0 {
            result = append(result, sort.Ints(l[i:i+1])[0])
        } else {
            result = append(result, v)
        }
    }
    return result
}