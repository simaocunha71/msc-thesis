    result := make([]int, 0)
    sort.Ints(l)

    for _, i := range l {
        if i != result[len(result)-1] {
            result = append(result, i)
        }
    }

    return result
}



