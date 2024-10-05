    result := make([]int, 0)
    for i, v := range l {
        if i%3 == 0 {
            sorted := make([]int, 0)
            for _, x := range l {
                if i%3 == 0 && x <= v {
                    sorted = append(sorted, x)
                }
            }
            sort.Ints(sorted)
            result = append(result, sorted[0])
        } else {
            result = append(result, v)
        }
    }
    return result
}