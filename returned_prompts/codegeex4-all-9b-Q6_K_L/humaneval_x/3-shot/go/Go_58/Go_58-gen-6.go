    l := append(l1, l2...)
    sort.Ints(l)
    result := make([]int, 0)
    for i := 0; i < len(l); i++ {
        if i == 0 {
            result = append(result, l[i])
        } else if l[i] != l[i-1] {
            result = append(result, l[i])
        }
    }
    return result
}



