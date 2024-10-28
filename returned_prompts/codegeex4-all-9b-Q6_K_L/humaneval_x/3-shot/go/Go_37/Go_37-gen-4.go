    even := make([]int, 0)

    for i := 0; i < len(l); i += 2 {
        even = append(even, l[i])
    }

    sort.Ints(even)

    result := make([]int, 0)
    result = append(result, even...)
    result = append(result, l[1:]...)
    return result
}

