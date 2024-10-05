    result := make([]int, len(l))
    for i := range l {
        if i%3 == 0 {
            indices := make([]int, 0)
            for j := range l {
                if j%3 == 0 {
                    indices = append(indices, j)
                }
            }
            sort.Ints(indices)
            result[i] = l[indices[0]]
        } else {
            result[i] = l[i]
        }
    }
    return result
}