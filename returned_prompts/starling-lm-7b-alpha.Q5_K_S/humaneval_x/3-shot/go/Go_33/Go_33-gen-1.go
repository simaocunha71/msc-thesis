    third_indices := make([]int, 0)
    for i := 0; i < len(l); i++ {
        if i%3 == 0 {
            third_indices = append(third_indices, i)
        }
    }
    sort.Slice(third_indices, func(i int, j int) bool {
        return l[third_indices[i]] < l[third_indices[j]]
    })
    result := make([]int, len(l))
    for i := 0; i < len(l); i++ {
        if i%3 != 0 {
            result[i] = l[i]
        }else {
            result[i] = l[third_indices[i]]
        }
    }
    return result
}



