    result := make([]int, 0)
    var last int
    for _, n := range numbers {
        if n != last {
            result = append(result, n)
            last = n
        }
    }
    return result
}



