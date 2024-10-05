    result := make([]int, 0)
    for i, v := range l {
        if i%3 == 0 {
            sort.Ints(&[]int{v})
            result = append(result, v)
        } else {
            result = append(result, v)
        }
    }
    return result
}