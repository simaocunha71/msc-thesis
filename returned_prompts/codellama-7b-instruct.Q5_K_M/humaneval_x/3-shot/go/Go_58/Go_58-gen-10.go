    result := make([]int, 0)

    for _, i := range l1 {
        if In(i, l2) {
            result = append(result, i)
        }
    }

    sort.Ints(result)
    return result
}



