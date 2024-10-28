    for i, _ := range lst {
        lst[i] = i
    }
    sort.Slice(lst, func(i, j int) bool {
        return lst[i] < lst[j]
    })

    result := make([]int, 0)
    for i := 0; i < len(lst); i++ {
        if i%2 == 0 {
            result = append(result, lst[len(lst)-i/2-1])
        }else {
            result = append(result, lst[i/2])
        }
    }
    return result
}



