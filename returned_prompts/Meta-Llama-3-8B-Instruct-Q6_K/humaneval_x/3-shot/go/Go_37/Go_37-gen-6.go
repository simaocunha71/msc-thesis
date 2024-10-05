    even := make([]int, 0)
    odd := l
    for _, v := range l {
        if v % 2 == 0 {
            even = append(even, v)
        }
    }
    sort.Ints(even)
    result := make([]int, 0)
    for i := 0; i < len(l); i++ {
        if i % 2 == 0 {
            result = append(result, even[i/2])
        } else {
            result = append(result, odd[i])
        }
    }
    return result
}