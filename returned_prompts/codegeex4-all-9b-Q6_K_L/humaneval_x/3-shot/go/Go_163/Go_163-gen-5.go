    result := make([]int, 0)
    var start int
    var end int

    if a < b {
        start = a
        end = b
    } else {
        start = b
        end = a
    }

    for i := start; i <= end; i++ {
        if i%2 == 0 {
            result = append(result, i)
        }
    }

    return result
}



