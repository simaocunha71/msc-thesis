    result := make([]int, 0)
    sort.Ints(lst)
    for i := 0; i < len(lst); i++ {
        if i%2 == 0 {
            result = append(result, lst[i])
        }else{
            result = append(result, lst[len(lst)-i-1])
        }
    }
    return result
}



