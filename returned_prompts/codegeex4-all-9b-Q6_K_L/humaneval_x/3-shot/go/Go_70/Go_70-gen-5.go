    sort.Ints(lst)
    result := []int{}
    for i := 0; i < len(lst); i++ {
        if i%2 == 0 {
            result = append(result, lst[i])
        } else {
            result = append([]int{lst[i]}, result...)
        }
    }
    return result
}

