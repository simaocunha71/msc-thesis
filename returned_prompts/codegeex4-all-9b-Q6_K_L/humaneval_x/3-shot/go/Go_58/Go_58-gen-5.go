    result := make(map[int]bool,0)
    for _, v := range l1 {
        result[v] = true
    }
    for _, v := range l2 {
        if _, ok := result[v]; ok {
            result[v] = true
        }
    }

    result_slice := make([]int, 0)
    for k, _ := range result {
        result_slice = append(result_slice, k)
    }
    sort.Ints(result_slice)
    return result_slice
}



