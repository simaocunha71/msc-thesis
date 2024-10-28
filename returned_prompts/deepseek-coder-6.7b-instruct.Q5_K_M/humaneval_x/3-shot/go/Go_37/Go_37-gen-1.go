    var even_indices []int
    var even_values []int

    for i:= range l {
        if i%2 == 0 {
            even_indices = append(even_indices, i)
            even_values = append(even_values, l[i])
        }
    }

    sort.Ints(even_values)

    for i, v := range even_values {
        l[even_indices[i]] = v
    }

    return l
}



