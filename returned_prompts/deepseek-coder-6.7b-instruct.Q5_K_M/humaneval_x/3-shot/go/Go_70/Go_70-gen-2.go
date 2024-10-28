    sort.Ints(lst)
    result := make([]int, len(lst))
    for i := 0; i < len(lst)/2; i++ {
        result[i*2] = lst[i]
        result[i*2+1] = lst[len(lst)-i-1]
    }
    if len(lst)%2 == 1 {
        result[len(lst)-1] = lst[len(lst)/2]
    }
    return result
}



