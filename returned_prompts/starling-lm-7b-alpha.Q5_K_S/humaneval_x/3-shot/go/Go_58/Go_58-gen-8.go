    result := make(map[int]int)
    for _, v := range l1 {
        result[v]++
    }
    for _, v := range l2 {
        result[v]++
    }
    var result_slice []int
    for k,_ := range result {
        if result[k] == 2 {
            result_slice = append(result_slice, k)
        }
    }

    sort.Ints(result_slice)
    return result_slice
}



