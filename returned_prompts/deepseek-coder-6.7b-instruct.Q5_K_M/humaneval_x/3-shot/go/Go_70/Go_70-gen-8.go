    sort.Ints(lst)
    result := make([]int, len(lst))
    for i := range lst {
        if i % 2 == 0 {
            result[i] = lst[i/2]
        } else {
            result[i] = lst[len(lst)-i/2-1]
        }
    }
    return result
}



