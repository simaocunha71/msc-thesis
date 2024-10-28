    result := make([]int, 0)
    sorted_result := make([]int, 0)
    for i, v := range l {
        if i % 3 == 0 {
            sorted_result = append(sorted_result, v)
        } else {
            result = append(result, v)
        }
    }
    sort.Ints(sorted_result)
    k := 0
    for i, v := range l {
        if i % 3 == 0 {
            l[i] = sorted_result[k]
            k++
        }
    }
    return l
}