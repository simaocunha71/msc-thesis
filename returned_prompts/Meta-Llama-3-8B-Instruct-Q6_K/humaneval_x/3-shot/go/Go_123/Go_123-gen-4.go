    result := make([]int, 0)
    i := n
    for i != 1 {
        if i % 2 == 1 {
            result = append(result, i)
        }
        if i % 2 == 0 {
            i = i / 2
        } else {
            i = 3*i + 1
        }
    }
    sort.Ints(result)
    return result
}