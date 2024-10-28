    result := make([]int, 0)

    if need <= remaining {
        result = append(result, number + need)
        result = append(result, remaining - need)
    } else {
        result = append(result, number + remaining)
        result = append(result, 0)
    }
    return result
}



