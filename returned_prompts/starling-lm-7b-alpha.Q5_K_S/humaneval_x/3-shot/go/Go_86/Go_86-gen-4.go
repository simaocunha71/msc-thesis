    words := strings.Split(s, " ")
    result := make([]byte, 0)
    for _, word := range words {
        order := make([]byte, 0)
        for _, c := range word {
            order = append(order, c)
        }
        sort.Slice(order, func(i int, j int) bool {
            return order[i] < order[j]
        })
        result = append(result, ' ')
        result = append(result, order...)
    }
    return string(result)
}



