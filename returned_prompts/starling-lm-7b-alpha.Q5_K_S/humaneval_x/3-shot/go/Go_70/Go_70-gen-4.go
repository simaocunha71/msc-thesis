    sort.Slice(lst, func(i int, j int) bool {
        return lst[i] < lst[j]
    })

    result := make([]int, 0)
    current_min := lst[0]
    current_max := lst[len(lst)-1]

    for current_min != current_max {
        result = append(result, current_min)
        result = append(result, current_max)
        var index_min int = 0
        for i := 0; i < len(lst); i++ {
            if lst[i] < current_min {
                index_min = i
            }
        }
        current_min = lst[index_min]
        lst = append(lst[:index_min], lst[index_min+1:]...)
        var index_max int = len(lst)-1
        for i := len(lst)-1; i >= 0; i-- {
            if lst[i] > current_max {
                index_max = i
            }
        }
        current_max = lst[index_max]
        lst = append(lst[:index_max], lst[index_max+1:]...)
    }
    result = append(result, current_min)
    return result
}



