    sort.Ints(l)
    result := []int{l[0]}
    for i := 1; i < len(l); i++ {
        if l[i] != l[i-1] {
            result = append(result, l[i])
        }
    }
    return result
}



