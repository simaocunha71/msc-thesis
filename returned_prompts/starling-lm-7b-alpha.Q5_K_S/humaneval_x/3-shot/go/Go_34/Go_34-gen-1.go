    unique_list := make([]int, 0)
    for _, v := range l {
        if !contains(unique_list, v) {
            unique_list = append(unique_list, v)
        }
    }
    sort.Slice(unique_list, func(i int, j int) bool {
        return unique_list[i] < unique_list[j]
    })
    return unique_list
}

func contains(l []int, v int) bool {
    for _, item := range l {
        if item == v {
            return true
        }
    }
    return false
}



