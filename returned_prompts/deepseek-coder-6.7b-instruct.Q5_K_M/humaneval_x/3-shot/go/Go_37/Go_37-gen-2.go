    even_indices := make([]int, 0)
    even_values := make([]int, 0)

    for i, v := range l {
        if i % 2 == 0 {
            even_indices = append(even_indices, i)
            even_values = append(even_values, v)
        }
    }

    sort.Ints(even_values)

    for i, v := range even_values {
        l[even_indices[i]] = v
    }

    return l
}



