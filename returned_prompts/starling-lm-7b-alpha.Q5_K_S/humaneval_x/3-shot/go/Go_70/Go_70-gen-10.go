    for i:= range lst{
        lst[i] = i
    }
    sort.Slice(lst, func(i int, j int) bool {
        return lst[i] < lst[j]
    })
    result := make([]int, 0)
    current_max := len(lst) - 1
    for i := 0; i < len(lst); i++ {
        if i%2 == 0 {
            result = append(result, lst[current_max])
            current_max--
        }else {
            result = append(result, lst[0])
            lst = lst[1:]
        }
    }
    return result
}



