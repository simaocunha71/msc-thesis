    for len(lst) > 1 {
        min_index := 0
        for i, v := range lst {
            if v < lst[min_index] {
                min_index = i
            }
        }
        max_index := 0
        for i, v := range lst {
            if v > lst[max_index] {
                max_index = i
            }
        }
        lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
        lst = lst[:len(lst)-1]
    }
    return lst
}



