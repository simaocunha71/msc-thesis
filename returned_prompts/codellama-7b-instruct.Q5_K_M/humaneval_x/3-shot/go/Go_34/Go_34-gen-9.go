    sort.Ints(l)
    var result []int

    for i := 0; i < len(l); i++ {
        if i == 0 {
            result = append(result, l[i])
        } else if l[i] != l[i-1] {
            result = append(result, l[i])
        }
    }
    return result
}



