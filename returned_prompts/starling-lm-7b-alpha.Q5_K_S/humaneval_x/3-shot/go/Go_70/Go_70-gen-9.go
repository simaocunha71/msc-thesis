    sort.Slice(lst, func(i int, j int) bool {
        return lst[i] < lst[j]
    })

    result := make([]int, 0)

    for i := 0; i < len(lst); i++ {
        result = append(result, lst[i])
        lst[i] = math.Max(0, lst[i]-1)
    }

    return result
}



