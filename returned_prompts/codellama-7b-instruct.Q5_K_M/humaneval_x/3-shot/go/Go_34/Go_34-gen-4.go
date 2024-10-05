    sort.Ints(l)
    unique_l := make([]int, 0)
    for i := 0; i < len(l); i++ {
        if i == 0 {
            unique_l = append(unique_l, l[i])
        } else if l[i] != l[i-1] {
            unique_l = append(unique_l, l[i])
        }
    }
    return unique_l
}



