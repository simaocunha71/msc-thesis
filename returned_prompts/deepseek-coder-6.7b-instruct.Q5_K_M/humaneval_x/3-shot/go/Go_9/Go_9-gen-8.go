    max_so_far  := math.MinInt64
    result  := make([]int, 0)

    for _, number  := range numbers  {
        if number > max_so_far  {
            max_so_far  = number
        }
        result = append(result, max_so_far )
    }

    return result
}



