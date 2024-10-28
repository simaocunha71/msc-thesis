    sort.Ints(l)
    result := make([]int, 0)
    last := -1 << 63
    for _, v := range l {
        if v != last {
            result = append(result, v)
            last = v
        }
    }
    return result
}



