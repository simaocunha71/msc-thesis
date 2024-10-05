    sort.Ints(lst)
    result := make([]int, 0)
    for i := 0; i < len(lst); i++ {
        if i%2 == 0 {
            result = append(result, lst[i])
        } else {
            result = append(result, lst[len(lst)-1-i])
        }
    }
    return result
}



